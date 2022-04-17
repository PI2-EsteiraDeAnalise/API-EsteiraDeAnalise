from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from extensions import db

class Maquina(db.Model):

  __tablename__ = 'maquinas'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(50), nullable=False)

  def serialize(self):
    return {
      'id': self.id,
      'nome': self.nome
    }

  def __repr__(self):
    return '<maquina {}>'.format(self.id)

class Placa(db.Model):

  __tablename__ = 'placas'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  data = db.Column(db.DateTime(), nullable=False)
  sucesso = db.Column(db.Boolean, nullable=False)
  maquina_id = Column(Integer, ForeignKey('maquinas.id'), nullable=False)

  def __init__(self, data, sucesso, maquina_id):
    self.data = data
    self.sucesso = sucesso
    self.maquina_id = maquina_id
  
  def serialize(self):
    return {
      'id': self.id,
      'data': self.data,
      'sucesso': self.sucesso,
      'maquina_id': self.maquina_id
    }

  def __repr__(self):
    return '<placa {} da maquina {}>'.format(self.id,self.maquina_id)
