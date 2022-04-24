#!/bin/bash

cd src/
FLASK_APP=app.py flask db init
FLASK_APP=app.py flask db migrate
FLASK_APP=app.py flask db upgrade
exit
