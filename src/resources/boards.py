from flask_restful import Resource
from flask import jsonify, request, make_response

from sqlalchemy.sql import extract

from extensions import db
from models import Board

from functools import reduce

class Boards(Resource):

  def get_successfully_boards(self, boards):
    if len(boards) == 0:
      return 0
    return reduce(lambda x, y: x + y, [1 if board.sucess else 0 for board in boards])
  
  def get_unsuccessfully_boards(self, boards):
    if len(boards) == 0:
      return 0
    return reduce(lambda x, y: x + y, [1 if not board.sucess else 0 for board in boards])
  
  def request_by_year_and_month(self, year, month):
    records = Board.query.filter(extract('year', Board.date) == year).filter(extract('month', Board.date) == month).all()
    return [{
      'quantity': len(records),
      'mes': int(month),
      'successfully': self.get_successfully_boards(records),
      'unsuccessfully': self.get_unsuccessfully_boards(records),
    }]

  def request_by_year(self, year):
    response = []
    for k in range(1, 13):
      records = Board.query.filter(extract('year', Board.date) == year).filter(extract('month', Board.date) == k).all()
      response.append({
        'quantity': len(records),
        'mes': k,
        'successfully': self.get_successfully_boards(records),
        'unsuccessfully': self.get_unsuccessfully_boards(records),
      })
    return response

  def get(self):
    year = request.args.get('year')
    month = request.args.get('month')
    response = []
    if not (month is None) and not (year is None):
      response = self.request_by_year_and_month(year, month)
    elif not (year is None):
      response = self.request_by_year(year)
    if len(response) == 0:
      return make_response(jsonify({'message': 'Nenhum registro encontrado'}), 404)
    return make_response(jsonify(response), 200)
    
  
  def post(self):
    args = request.get_json()
    board_record = Board(sucess=args['sucess'])
    db.session.add(board_record)
    db.session.commit()
    return Board.serialize(board_record), 201
