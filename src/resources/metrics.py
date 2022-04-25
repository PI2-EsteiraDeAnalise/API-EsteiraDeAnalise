from flask_restful import Resource
from flask import jsonify, request, make_response

from extensions import db

class Metrics(Resource):

  def read_file(self):
    with open('/app/src/assets/infos.txt', 'r') as f:
      return f.readlines()
 
  def serialize(self, records):
    response = []
    for record in records:
      response.append(
        {
          'metric': record.split(',')[0],
          'description': record.split(',')[1].replace('\n', ''),
        }
      )
    return jsonify(response)
  
  def get(self): 
    records = self.read_file()
    return make_response(self.serialize(records), 200)
  
 