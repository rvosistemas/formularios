from config import db
import datetime
from sqlalchemy.orm import declarative_base, backref, relationship
from sqlalchemy import Column, Integer, ForeignKey, DateTime
Base = declarative_base()


# class Logs(Base):
class Logs(db.Model):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    created = Column(
        DateTime, nullable=False,
        default=datetime.datetime.utcnow)
    field_id = Column(Integer, ForeignKey('fields.id'))
    field = relationship("Fields", backref=backref("child", uselist=False))

    def __repr__(self):
        return "<Logs(field_id='%s', created='%s')>" % (
            self.field_id, self.created)
