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
    if year is None or month is None:
      return []
    response = []
    for k in range(1,27,5):
      initial_date = '{}-{}-{}'.format(year, month, k)
      final_date = '{}-{}-{}'.format(year, month, k + 4)
      records = Board.query.filter(Board.date >= initial_date, Board.date <= final_date).all()
      response.append({
        'day': '{}-{}'.format(k, k+4),
        'month': int(month),
        'year': int(year),
        'successfully': self.get_successfully_boards(records),
        'unsuccessfully': self.get_unsuccessfully_boards(records),
      })
    return response

  def get(self):
    year = request.args.get('year')
    month = request.args.get('month')
    response = self.request_by_year_and_month(year, month)
    if len(response) == 0:
      return make_response(jsonify({'message': 'Nenhum registro encontrado'}), 404)
    return make_response(jsonify(response), 200)
    
  
  def post(self):
    args = request.get_json()
    board_record = Board(sucess=args['sucess'])
    db.session.add(board_record)
    db.session.commit()
    return Board.serialize(board_record), 201
