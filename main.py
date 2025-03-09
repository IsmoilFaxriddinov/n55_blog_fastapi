from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routers import posts, users

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)

@app.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/docs")