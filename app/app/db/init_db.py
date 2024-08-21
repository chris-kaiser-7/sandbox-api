from pymongo.database import Database

from app import crud, schemas
from app.core.config import settings
import logging


async def init_db() -> None:
    user = await crud.user.get_by_email(email=settings.FIRST_SUPERUSER)
    if not user:
        # Create user auth
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            full_name=settings.FIRST_SUPERUSER,
        )
        user = await crud.user.create(obj_in=user_in)  # noqa: F841
