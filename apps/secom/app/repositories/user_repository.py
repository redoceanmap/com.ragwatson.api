import logging
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from secom.app.models.user_model import UserModel
from secom.app.schemas.user_schema import UserSchema

logger = logging.getLogger(__name__)


class UserRepository:

    async def save_user(self, session: AsyncSession, user_schema: UserSchema) -> UserModel:
        user = UserModel(
            user_id=user_schema.userId,
            password=user_schema.password,
            nickname=user_schema.nickname,
            email=user_schema.email,
            role=user_schema.role,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        logger.info("[UserRepository] save_user 완료 — userId=%s", user.user_id)
        return user

    async def find_by_email(self, session: AsyncSession, email: str) -> UserModel | None:
        result = await session.execute(select(UserModel).where(UserModel.email == email))
        return result.scalars().first()