from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)

    bio = Column(Text, nullable=True)
    profile_picture = Column(String(500), nullable=True)

    is_superuser = Column(Boolean(), default=False)
    is_active = Column(Boolean(), default=True)
    is_verified = Column(Boolean(), default=False)

    blogs = relationship("Blog", back_populates="author")
