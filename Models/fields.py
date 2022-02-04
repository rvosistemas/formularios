from config import db
import datetime
from sqlalchemy.orm import declarative_base, backref, relationship
from sqlalchemy import Column, Integer, String
Base = declarative_base()


# class Logs(Base):
class Fields(db.Model):
    __tablename__ = 'fields'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    city = Column(String(80), nullable=False)

    def __repr__(self):
        return "<Fields(full_name='%s', email='%s', city='%s)>" % (
            self.full_name, self.email, self.city)
