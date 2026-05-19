import logging
from sqlalchemy.ext.asyncio import AsyncSession
from secom.app.models.user_model import UserModel
from secom.app.repositories.user_repository import UserRepository
from secom.app.schemas.user_schema import UserSchema, LoginSchema

logger = logging.getLogger(__name__)


class UserService:

    def __init__(self) -> None:
        self.user_repository = UserRepository()

    async def save_user(self, session: AsyncSession, user_schema: UserSchema) -> UserModel:
        user = await self.user_repository.save_user(session, user_schema)
        logger.info("[UserService] save_user 레이어 완료 — userId=%s", user.user_id)
        return user

    async def login_user(self, session: AsyncSession, login_schema: LoginSchema) -> UserModel | None:
        user = await self.user_repository.find_by_email(session, login_schema.email)
        logger.info("[UserService] login_user 레이어 완료 — email=%s", login_schema.email)
        return user