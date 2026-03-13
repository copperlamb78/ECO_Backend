from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def homepage():
    return {"mensagem": "ECO"}