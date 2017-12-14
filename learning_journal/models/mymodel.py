"""."""
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'Entry'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(DateTime, default=datetime.now())

    def to_dict(self):
        return{'id': self.id,
               'title': self.title,
               'body': self.body,
               'creation_date': self.creation_date.strftime('%A, %d %B, %Y, %I:%M %p')
               }
