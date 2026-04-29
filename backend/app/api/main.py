from fastapi import APIRouter

from app.api.routes import cmd, login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(cmd.router)
