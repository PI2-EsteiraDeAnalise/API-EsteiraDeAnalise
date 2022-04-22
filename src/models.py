from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from extensions import db

class Board(db.Model):

  __tablename__ = 'boards'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  date = db.Column(db.Date(), nullable=False, default=db.func.current_date())
  sucess = db.Column(db.Boolean, nullable=False)

  def __init__(self, sucess):
    self.sucess = sucess
  
  def serialize(self):
    return {
      'id': self.id,
      'date': self.date.__str__(),
      'sucess': self.sucess,
    }

  def __repr__(self):
    return '<board: {}>'.format(self.id)

class Tag(db.Model):

  __tablename__ = 'tags'

  name = db.Column(db.String(50), primary_key=True, nullable=False)

  def __init__(self, name):
    self.name = name
  
  def serialize(self):
    return {
      'name': self.name,
    }
  
  def __repr__(self):
    return '<tag: {}>'.format(self.name)
