from app.utils import create_jwt


def create(user_id: int) -> str:
    token = create_jwt({"sub": str(user_id)})
    return token
