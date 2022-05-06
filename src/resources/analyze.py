from flask_restful import Resource
from flask import jsonify, request
from mjpeg.server import MJPEGResponse
from mjpeg.client import MJPEGClient
from ../utils/analyze import predicao
import requests
import os

from extensions import db

class Analyze(Resource):
    def get(self):
        coordinates = requests.get(os.getenv("API_URL") + "/coordinates")
        image = requests.get(os.getenv("API_URL") + "/relay")
        return predicao(coordinates, image)
