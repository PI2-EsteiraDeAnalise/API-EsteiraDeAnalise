#!/bin/bash

cd src/
FLASK_APP=app.py flask db init
FLASK_APP=app.py flask db migrate
FLASK_APP=app.py flask db upgrade
libcamera-vid -t 0 --inline --codec mjpeg -o - \
  | python3 -m mjpeg_http_streamer -p 8080
python3 app.py
