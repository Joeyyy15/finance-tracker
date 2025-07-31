from fastapi import APIRouter

router = APIRouter

@router.get("/income")
def get_income():
    return {"message": "Income endpoint is working"}