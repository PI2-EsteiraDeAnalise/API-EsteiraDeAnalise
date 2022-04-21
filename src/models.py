from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from extensions import db

class Placa(db.Model):

  __tablename__ = 'placas'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  data = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
  sucesso = db.Column(db.Boolean, nullable=False)

  def __init__(self, sucesso):
    self.sucesso = sucesso
  
  def serialize(self):
    return {
      'id': self.id,
      'data': self.data.__str__(),
      'sucesso': self.sucesso,
    }

  def __repr__(self):
    return '<placa: {}>'.format(self.id)

class Tag(db.Model):

  __tablename__ = 'tags'

  nome = db.Column(db.String(50), primary_key=True, nullable=False)

  def __init__(self, nome):
    self.nome = nome
  
  def serialize(self):
    return {
      'nome': self.nome,
    }
  
  def __repr__(self):
    return '<tag: {}>'.format(self.nome)
