from flask_restful import Resource
from flask import jsonify, request

from extensions import db
from models import Placa

class Placas(Resource):
  def get(self):
    records = Placa.query.all()
    return jsonify([Placa.serialize(record) for record in records])
  
  def post(self):
    args = request.get_json()
    placa_record = Placa(sucesso=args['sucesso'])
    db.session.add(placa_record)
    db.session.commit()
    return Placa.serialize(placa_record), 201
