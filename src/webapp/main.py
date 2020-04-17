import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from src.webapp.db import get_db, query_db

"""
    Adds a main Blueprint for use in the app.
    See : https://flask.palletsprojects.com/en/1.1.x/tutorial/views/
"""

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home():
    images = query_db('select * from images')
    return render_template('list_images.html', images=images)


@bp.route('/image')
def image():
    id = request.args.get('id')
    image = query_db("SELECT * FROM images WHERE id=:id", {'id':id})
    print(image)
    if(image):
        image = image[0]
        scores = query_db("SELECT u.username, COUNT(p.id) as score FROM users as u, points as p WHERE u.id=p.user_id AND p.image_id=:image_id GROUP BY u.id ORDER BY score DESC", {'image_id':id})
        return render_template('single_image.html', image=image, scores=scores)
    else:
        return "image not found"

