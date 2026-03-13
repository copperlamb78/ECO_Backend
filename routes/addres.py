from fastapi import APIRouter
router = APIRouter()

@router.get("/addres")
def addres():
    return {"message": "página de localização"}