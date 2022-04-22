from flask_restful import Resource
from flask import jsonify, request, make_response

from extensions import db
from models import Metric

class Metrics(Resource):
  def get(self):
    records = Metric.query.all()
    if len(records) == 0:
      return make_response(jsonify({'message': 'Nenhum registro encontrado'}), 404)
    return make_response(jsonify([Metric.serialize(record) for record in records]), 200)

  def post(self):
    args = request.get_json()
    metric_record = Metric(metric=args['metric'], description=args['description'])
    db.session.add(metric_record)
    db.session.commit()
    return Metric.serialize(metric_record), 201