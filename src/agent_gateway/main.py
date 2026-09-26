from fastapi import FastAPI
from agent_gateway.routers import health
from agent_gateway.routers import tools

app = FastAPI()

app.include_router(health.router)
app.include_router(tools.router)
