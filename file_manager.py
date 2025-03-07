import csv
import os
import uuid

async def read_file(filename:str) -> list:
    try:
        with open(file=filename, mode='r', encoding='UTF-8') as file:
            reader = csv.reader(csvfile=file)
            return list(reader)
    except Exception as e:
        print(e)
        return list()

directory = "user"
filename = "user/csv"


def append_row(filename: str, row: list) -> bool:
    try:
        file_exists = os.path.exists(filename)
        with open(filename, mode='a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["uuid", "username", "age", "phone_number"])
            if len(row) == 3:
                row.insert(0, str(uuid.uuid4()))
            writer.writerow(row)
        return True
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        return False

