from flask_restful import Resource
from flask import jsonify, request

from extensions import db
from models import Maquina

class Maquinas(Resource):
  def get(self):
    records = Maquina.query.all()
    return jsonify([Maquina.serialize(record) for record in records])
  
  def post(self):
    args = request.get_json()
    maquina_record = Maquina(nome=args['nome'])
    db.session.add(maquina_record)
    db.session.commit()
    return Maquina.serialize(maquina_record), 201
