from flask_restful import Resource
from flask import jsonify, request
from mjpeg.server import MJPEGResponse
from mjpeg.client import MJPEGClient
import os

from extensions import db


class Relay(Resource):
    def get(self):
        return MJPEGResponse(self.relay())

    def relay(self):
        url = os.getenv("MJPEG_URL")

        # Create a new client thread
        client = MJPEGClient(url)

        # Allocate memory buffers for frames
        bufs = client.request_buffers(65536, 50)
        for b in bufs:
            client.enqueue_buffer(b)

        # Start the client in a background thread
        client.start()

        while True:
            buf = client.dequeue_buffer()
            yield memoryview(buf.data)[:buf.used]
            client.enqueue_buffer(buf)
