#!/bin/sh
export FLASK_APP=src/webapp
export FLASK_ENV=development
flask init-db
#flask insert-db
flask run --host=0.0.0.0
