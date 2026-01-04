from sqlalchemy.orm import Session

from schemas.user import CreateUser
from db.models.users import User
from core.hashing import Hasher


def create_new_user(user:CreateUser, db:Session):
    new_user = User(
            username = user.username,
            email = user.email,
            password = Hasher.get_password_hash(user.password),
            )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
