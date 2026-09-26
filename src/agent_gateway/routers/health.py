from fastapi import APIRouter,status
from pydantic import BaseModel

router = APIRouter()

class HealthCheck(BaseModel):
  status:str = "OK"

@router.get("/health", status_code=status.HTTP_200_OK, response_model=HealthCheck)
def get_health() -> HealthCheck:
    """Simple liveness probe to verify the application server is up and running."""
    return HealthCheck(status = "OK")
