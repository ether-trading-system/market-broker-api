from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


@router.get("/accounts", tags=["accounts"])
async def read_accounts():
    return [{"name": "Alice"}, {"name": "Bob"}]