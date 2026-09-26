from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/tools")
def list_tools() -> list[dict]:
  return []

@router.post("tools/{id}/execute")
def execute_tool(id: str) -> dict:
  return {"tool" : id, "status": "Not Implemented" }
