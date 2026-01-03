import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.base_class import Base


class Blog(Base):
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False)
    content = Column(Text, nullable=True)
    excerpt = Column(Text, nullable=True)

    author_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    author = relationship("User", back_populates="blogs")

    status = Column(String, default="draft")
    is_featured = Column(Boolean, default=False)

    featured_image = Column(String, nullable=True)

    published_at = Column(DateTime, nullable=True)
