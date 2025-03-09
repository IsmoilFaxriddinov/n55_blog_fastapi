from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/tests")
async def get_tests():
    return "Hello World"