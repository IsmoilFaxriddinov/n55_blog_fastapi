from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=['salom']
)

@router.get('/tests')
async def test():
    return "Hello"