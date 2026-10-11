import os
import logging
import datetime
import jwt

logger = logging.getLogger(__name__)

SECRET_KEY = os.environ["JWT_SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 15))


def create_jwt_token(data: dict, expires_in_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    now = datetime.datetime.now(datetime.timezone.utc)
    to_encode = {
        **data,
        "iat": now,
        "exp": now + datetime.timedelta(minutes=expires_in_minutes),
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        logger.info("JWT expired")
        return None
    except jwt.InvalidTokenError as e:
        logger.warning("Invalid JWT: %s", e)
        return None
