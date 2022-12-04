from fastapi import APIRouter
# from src.endpoints.user import user_endpoint as user
from src.endpoints.auth import auth_endpoint as auth

router = APIRouter()
# router.include_router(user.router)
router.include_router(auth.router)
