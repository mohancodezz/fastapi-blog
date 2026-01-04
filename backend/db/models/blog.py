import uuid
from enum import Enum
from datetime import datetime

from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.base_class import Base


class BlogStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class Blog(Base):
    title = Column(String(200), nullable=False)
    slug = Column(String(250), unique=True, index=True, nullable=False)
    content = Column(Text, nullable=False)
    excerpt = Column(Text, nullable=True)

    author_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    author = relationship("User", back_populates="blogs")

    status = Column(String, default=BlogStatus.DRAFT.value)
    is_featured = Column(Boolean, default=False)
    featured_image = Column(String, nullable=True)
    published_at = Column(DateTime, nullable=True)

    meta_description = Column(String(160), nullable=True)
    read_time = Column(Integer, nullable=True)
    view_count = Column(Integer, default=0)
