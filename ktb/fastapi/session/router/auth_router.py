from fastapi import APIRouter, Request
from controller.auth_controller import login_user, logout_user

router = APIRouter(prefix="/auth", tags=["auth"]) #prefix 때문에 router에 연결되는 모든 주소는 자동적으로 /auth가 붙음

@router.post("/login")
async def login(request: Request):
    return await login_user(request)

@router.delete("/logout")
async def logout(request: Request):
    return await logout_user(request)