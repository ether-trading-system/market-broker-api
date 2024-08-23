from fastapi import APIRouter

router = APIRouter()


@router.get("/accounts", tags=["accounts"])
async def read_accounts():
    return [{"name": "Alice"}, {"name": "Bob"}]
