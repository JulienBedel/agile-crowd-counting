export FLASK_APP=src/webapp
export FLASK_ENV=development
flask init-db
flask insert-db
flask run