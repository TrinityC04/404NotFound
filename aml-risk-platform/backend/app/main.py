from fastapi import Depends, FastAPI

from app.shared.auth.dependencies import (
    get_current_user,
    require_role,
)

app = FastAPI(
    title="AML Risk Intelligence Platform",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {
        "name": "AML Risk Intelligence Platform",
        "status": "ok",
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }

@app.get("/api/v1/auth/me")
async def get_me(
    current_user: dict = Depends(get_current_user),
):
    return {
        "id": current_user.get("sub"),
        "username": current_user.get("preferred_username"),
        "email": current_user.get("email"),
        "roles": current_user.get("realm_access", {}).get("roles", []),
    }

@app.get("/api/v1/admin-test")
async def admin_test(
    current_user: dict = Depends(require_role("admin")),
):
    return {
        "message": "You have admin access",
        "username": current_user.get("preferred_username"),
    }

