import csv
import os
import uuid
from fastapi import FastAPI, HTTPException, Query
from typing import Annotated
from schemas import UserIn, UserOut
from file_manager import append_row, read_file

app = FastAPI()

@app.get("/users/")
async def get_users(skip: int = 0, limit: int = Query(2, le=10, ge=2), q: str | None = Query(None, max_length=100)):
    filename = "user/csv"
    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="Foydalanuvchilar bazasi topilmadi")
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            users = list(reader)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Faylni oqishda xatolik: {str(e)}")
    if q:
        users = [user for user in users if q.lower() in user[1].lower()]
    users = users[skip: skip + limit]
    return [
        UserOut(uuid=user[0], username=user[1], age=user[2], phone_number=user[3])
        for user in users if len(user) >= 4]


@app.post("/users/", status_code=201)
async def add_user(user: UserIn):
    if append_row(filename='user/csv', row=[uuid.uuid4(), user.username, user.age, user.phone_number]):
        return "User is added"
    return "Error"

@app.get("/users/{username}")
async def get_user(username: str):
    filename = "user/csv"

    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="Foydalanuvchilar bazasi topilmadi")
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            users = list(reader)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Faylni oqishda xatolik: {str(e)}")
    for user in users:
        if len(user) >= 4 and user[1].strip().lower() == username.strip().lower():
            return UserOut(uuid=user[0], username=user[1], age=user[2], phone_number=user[3])

    raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")
