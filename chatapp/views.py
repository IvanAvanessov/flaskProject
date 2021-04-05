from flask import Blueprint, render_template, request, redirect, url_for
from flask import jsonify
from datetime import datetime

chatapp_url = Blueprint('chatapp',
                        __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/chatapp/static')

from .models import User
import os
from main import db
from sqlalchemy import Table, Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
import string, random, config
from .funcs import *
from .funcs import get_messages_for_room_jsonify
import json
from ccyapp.views import get_ccy_rate_for

@chatapp_url.route('/', methods=['GET'])
def index():
    letters = string.ascii_letters
    room_name = ''.join(random.choice(letters) for i in range(10))
    print(os.path.abspath(os.path.dirname(__file__)))

    return render_template('index.html', name='hujaba')


@chatapp_url.route('/', methods=['POST'])
def create_room_POST():
    try:
        roomID = create_room()
        return roomID
    except RuntimeError:
        return 'False'


@chatapp_url.route('/<roomID>/', methods=['GET'], strict_slashes=False)
def join_room_GET(roomID):
    print("join_room_get")
    if len(roomID) == 0:
        return 'BLANK'
    else:
        room = get_room_by_ID(roomID)
        if room is not None:
            return render_template('room.html', roomID=roomID, roomTableName=room.__tablename__)
        else:
            return render_template('404.html', roomID=roomID)


@chatapp_url.route('/<roomID>', methods=['POST'])
def check_room_exist(roomID):
    print('this is here')
    try:
        room = get_room_by_ID(roomID)
        if room is not None:
            return 'True'
        else:
            return 'False'
    except RuntimeError:
        print('Database Error occurred in join_room_POST')
        return 'ERROR'


@chatapp_url.route('/<roomID>/msg', methods=['POST'])
def send_message(roomID):
    message = request.form.get('message')
    nickname = request.form.get('nickname')
    postedRoomID = request.form.get('roomID')
    if postedRoomID != roomID or message is None or nickname is None:
        return 'invalid message request'
    room = get_room_by_ID(roomID)
    if room is not None:
        if add_message_to_room(message, nickname, room):
            return 'True'
        else:
            return 'False'
    else:
        return 'Corrupt POST request'


@chatapp_url.route('/<roomID>/msg', methods=['GET'])
def get_messages(roomID):
    print(request.args.get('roomID'))
    messageID = (request.args.get('messageID'))
    try:
        room = get_room_by_ID(roomID)
        if room is not None:
            messages = get_messages_for_room(room, messageID)
            messages = [message.to_dict() for message in messages]
            for message in messages:
                message['exchangeRate'] = get_ccy_rate_for('USDEUR')
            return jsonify(messages)
        else:
            return 'False'
    except RuntimeError:
        return 'ERROR'
