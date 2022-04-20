from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime

from extensions import db

class Placa(db.Model):

  __tablename__ = 'placas'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  data = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
  sucesso = db.Column(db.Boolean, nullable=False)

  def __init__(self, sucesso):
    self.sucesso = sucesso
  
  def serialize(self):
    return {
      'id': self.id,
      'data': self.data,
      'sucesso': self.sucesso,
    }

  def __repr__(self):
    return '<placa: {}>'.format(self.id)
