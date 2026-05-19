import logging
from sqlalchemy.ext.asyncio import AsyncSession
from secom.app.models.user_model import UserModel
from secom.app.services.user_service import UserService
from secom.app.schemas.user_schema import UserSchema, LoginSchema

logger = logging.getLogger(__name__)


class UserController:

    def __init__(self) -> None:
        self.user_service = UserService()

    async def save_user(self, session: AsyncSession, user_schema: UserSchema) -> UserModel:
        user = await self.user_service.save_user(session, user_schema)
        logger.info("[UserController] save_user 레이어 완료 — userId=%s", user.user_id)
        return user

    async def login_user(self, session: AsyncSession, login_schema: LoginSchema) -> UserModel | None:
        user = await self.user_service.login_user(session, login_schema)
        logger.info("[UserController] login_user 레이어 완료 — email=%s", login_schema.email)
        return user 