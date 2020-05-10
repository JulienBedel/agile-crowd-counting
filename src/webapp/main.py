import os
import imghdr

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, send_from_directory
)

from src.webapp.db import get_db, query_db
from src.count.counter import count

"""
    Adds a main Blueprint for use in the app.
    See : https://flask.palletsprojects.com/en/1.1.x/tutorial/views/
"""

bp = Blueprint('main', __name__, url_prefix='/')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@bp.route("/upload")
def new():
    return render_template("upload.html")


@bp.route("/images", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)
    
    uploads = request.files.getlist("file")
    
    print("received " + str(uploads))

    if uploads:
        for upload in uploads:

            if (imghdr.what(upload)== 'jpeg' or imghdr.what(upload)=='png' or imghdr.what(upload)=='bmp'):
                filename = upload.filename
                destination = "/".join([target, filename])
                counted_points = count(target)
                db = get_db()
                db.execute('INSERT INTO images (path, count) VALUES (?, ?)',(filename, counted_points) )
                db.commit()
                upload.save(destination)
                return render_template("upload_success.html")

            else:
                return render_template("upload_fail.html")
    else:
        return render_template("upload_fail.html")    



# routes for image view (single + gallery)

@bp.route('/images/<filename>')
def show_image(filename):
    return send_from_directory("images", filename)