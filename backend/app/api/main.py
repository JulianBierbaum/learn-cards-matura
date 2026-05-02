from fastapi import APIRouter

from app.api.routes import cmd, login, user, card

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, tags=["user"])
api_router.include_router(card.router, tags=["card"])
api_router.include_router(cmd.router)
