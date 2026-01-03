from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean(), default=True)
    is_active = Column(Boolean(), default=True)
    is_verified = Column(Boolean(), default=True)
    blogs = relationship("Blog", back_populates="author")
