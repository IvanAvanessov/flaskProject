from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
import os
from main import db
from sqlalchemy import Table, Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
import string, random, config
from .funcs import create_room

chatapp_url = Blueprint('chatapp', __name__, template_folder='templates')



@chatapp_url.route('/', methods=['GET'])
def index():
    letters = string.ascii_letters
    room_name = ''.join(random.choice(letters) for i in range(10))

    #user = User(username='van4es')

    #room = create_room(room_name)
    ##db.create_all()
    #db.session.commit()
    #room1 = room(message='test')
    #db.session.add(room1)
    #db.session.commit()
    print(os.path.abspath(os.path.dirname(__file__)))

    return render_template('index.html', name='hujaba')

@chatapp_url.route('/', methods=['POST'])
def create_room_POST():
    roomID = create_room()
    if roomID is not None:
        return redirect("/")
    return


@chatapp_url.route('/chatroom', methods=['GET'])
def test_method():
    print(request.method)
    return 'huj2'
