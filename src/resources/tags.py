from flask_restful import Resource
from flask import jsonify, request

from extensions import db
from models import Tag

class Tags(Resource):
  def get(self):
    records = Tag.query.all()
    return jsonify([Tag.serialize(record) for record in records])