from fastapi import Depends, FastAPI

from users.db.db import User
from users.model.schemas import UserRead, UserCreate, UserUpdate
from users.service.service import auth_backend, current_active_user, fastapi_users


def include_router(app: FastAPI):
    app.include_router(
        fastapi_users.get_auth_router(auth_backend, requires_verification=True),
        prefix="/auth/jwt",
        tags=["auth"],
    )

    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"],
    )

    app.include_router(
        fastapi_users.get_verify_router(UserRead),
        prefix="/auth",
        tags=["auth"],
    )

    app.include_router(
        fastapi_users.get_reset_password_router(),
        prefix="/auth",
        tags=["auth"],
    )

    app.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate, requires_verification=True),
        prefix="/users",
        tags=["users"],
    )

    @app.get("/authenticated-route")
    async def authenticated_route(user: User = Depends(current_active_user)):
        return {"message": f"Hello {user.email}!"}
