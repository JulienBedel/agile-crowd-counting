"""
    Adds a main Blueprint the app, following Flask official Tutorial.
    See : https://flask.palletsprojects.com/en/1.1.x/tutorial/views/
"""

import os
import json
import imghdr

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, send_from_directory, abort
from flask_socketio import SocketIO, emit, send

from src.webapp.db import get_db, query_db
from src.count.counter import count
from . import socketio

bp = Blueprint('main', __name__, url_prefix='/')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@bp.route('/')
def index():
    return render_template("index.html")


# routes for image upload

@bp.route("/new")
def new():
    return render_template("upload.html")


@bp.route("/images", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)
    
    uploads = request.files.getlist("file")
    
    if uploads:
        for upload in uploads:

            if (imghdr.what(upload)== 'jpeg' or imghdr.what(upload)=='png' or imghdr.what(upload)=='bmp'):
                filename = upload.filename
                destination = "/".join([target, filename])
                upload.save(destination)
                counted_points = count(destination)
                db = get_db()
                db.execute('INSERT INTO images (path, count) VALUES (?, ?)',(filename, counted_points) )
                db.commit()
                return render_template("upload_success.html")

            else:
                return render_template("upload_fail.html")
    else:
        return render_template("upload_fail.html")    




# routes for image view (single + gallery)

@bp.route('/images/<filename>')
def show_image(filename):
    return send_from_directory("images", filename)


@bp.route('/play')
def get_gallery():
    images = db_get_all_images()
    return render_template("gallery.html", images=images)

    

# routes for counting of image "id"

@bp.route('/play/<id>', methods = ['GET', 'POST'])
def play_image(id):
    
    # GET = display counting page, POST = insert new point
    image = db_get_image(id)
    if(not image):
        return abort(404)

    if request.method == 'GET':
        image = image[0]
        scores = db_get_all_scores_image(id)
        points = db_get_points(id)
        points_json = json.dumps(points)
        return render_template('play_image.html', image=image, scores=scores, points=points_json)

    if request.method == 'POST':

        # 1. parse POST data,  2. insert into db (+ check if user exists), 3. sends updated point + scores back to web instances
        
        try:
            data = request.get_json()
        except (ValueError):
            return abort(400)

        if not data or not all (k in data for k in ("username", "x_coord", "y_coord")):
            return abort(400)
        
        username = data['username']
        x_coord = data['x_coord']
        y_coord = data['y_coord']
        image_id = id

        if(not db_check_user_exists(username)):
            db_insert_new_user(username)
        
        user_id = db_get_user_id(username)
        
        db_insert_new_point(x_coord, y_coord, user_id, image_id)

        scores =  db_get_all_scores_image(image_id)
        scores_json = json.dumps(scores)
        socketio.emit('newpoint', {'x_coord': x_coord, 'y_coord': y_coord, 'username': username, 'scores': scores_json}, namespace='/test')  
        return scores_json, 200
        

# websockt handling

@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


# database interaction

def db_get_all_images():
    return query_db('SELECT * FROM images')

def db_get_image(id):
    return query_db("SELECT * FROM images WHERE id=:id", {'id':id})

def db_get_image_by_name(filename):
    return query_db("SELECT * FROM images WHERE path=:filename", {'filename':filename}) 

def db_get_points(id):
    return query_db("SELECT x_coord , y_coord FROM points where image_id=:id",{'id':id}) 

def db_get_user_id(username):
    query = query_db("SELECT id FROM users WHERE username=:username", {'username':username})
    if query:
        return query[0]['id']
    else:
        return None

def db_check_user_exists(username):
    if(db_get_user_id(username)):
        return True
    else:
        return False

def db_insert_new_user(username):
    db = get_db()
    db.execute('INSERT INTO users (username) VALUES (?)', (username,))
    db.commit()

def db_insert_new_point(x_coord, y_coord, user_id, image_id):
    db = get_db()
    db.execute('INSERT INTO points (x_coord, y_coord, user_id, image_id) VALUES (?,?,?,?)', (x_coord, y_coord, user_id, image_id))
    db.commit()

def db_get_all_scores_image(image_id):
    query_string = """
    SELECT u.username, COUNT(p.id) as score FROM users as u, points as p 
    WHERE u.id=p.user_id AND p.image_id=:image_id 
    GROUP BY u.id ORDER BY score DESC
    """
    return query_db(query_string, {'image_id':image_id})

def get_user_score_image(image_id, user_id):
    query_string = """
    SELECT u.username, COUNT(p.id) as score FROM users as u, points as p 
    WHERE u.id=p.user_id AND p.image_id=:image_id 
    AND u.id=:user_id 
    GROUP BY u.id ORDER BY score DESC
    """
    return query_db(query_string, {'image_id':image_id, 'user_id':user_id})