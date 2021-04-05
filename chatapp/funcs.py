import string, random
from datetime import datetime
from .models import Rooms, create_room_model
from main import db
from sqlalchemy import exc, MetaData
import json
from flask import jsonify
from apikeys import *
import requests

roomIDTableNameLength = 8
roomIDLength = 6
listOfActiveRooms = {}


def create_room() -> str:
    doesRoomExist = True  # has to be true for first pass of loop
    counter = 0
    while doesRoomExist and counter < 10:
        letters = string.ascii_uppercase
        roomID = ''.join(random.choice(letters) for i in range(roomIDLength))
        createdTime = datetime.now()
        lastUpdatedTime = datetime.now()
        currentUsers = 0
        letters = string.ascii_letters
        roomTableName = roomID + '_' + ''.join(random.choice(letters) for i in range(roomIDTableNameLength))
        doesRoomExist = get_room_by_ID(roomID) is not None

        if not doesRoomExist:
            newRoom = Rooms(roomID=roomID, createdTime=createdTime, lastUpdatedTime=lastUpdatedTime,
                            currentUsers=currentUsers,
                            roomTableName=roomTableName)
            db.session.add(newRoom)
            listOfActiveRooms[roomTableName] = create_room_model(roomTableName)
            try:
                db.create_all()
                db.session.commit()
            except exc.SQLAlchemyError:
                print('Error while creating table in DB')  # print to error Log
            return roomID
        counter += 1
    return 'Error in the while Loop'


def get_room_by_ID(roomID):
    try:
        roomEntry = db.session.query(Rooms).filter_by(roomID=roomID).first()
        if roomEntry is not None:
            if roomEntry.roomTableName not in listOfActiveRooms:
                listOfActiveRooms[roomEntry.roomTableName] = create_room_model(roomEntry.roomTableName)
            return listOfActiveRooms[roomEntry.roomTableName]
        else:
            return None
    except exc.SQLAlchemyError:
        print('Error reading from the database')  # print to log
        return None


def add_message_to_room(message, nickname, room):
    messageTime = datetime.now()
    newMessage = room(username=nickname, messageTime=messageTime, message=message)
    try:
        db.session.add(newMessage)
        db.session.commit()
        return True
    except exc.SQLAlchemyError:
        return False


def get_messages_for_room(room, messageID=None):
    if messageID is not None:
        messages = db.session.query(room).filter(room.id > messageID).order_by(room.id.asc()).all()
    else:
        messages = db.session.query(room).order_by(room.id.asc()).all()
    return list(messages)


def custom_JSON_converter(item):
    if isinstance(item, datetime):
        return item.__str__()


def get_messages_for_room_jsonify(room, messageID=None):
    messages = get_messages_for_room(room, messageID)
    messages = [message.to_dict() for message in messages]

    return jsonify([message.to_dict() for message in messages])


def get_ccy_rate_for(ccyPair):  # in format 'CCY1_CCY1'
    #fullURL = ccyAPIURLhead + ccyPair + ccyAPIURLtail + ccyAPIkey
    fullURL = '/ccy/USDEUR'
    r = requests.get(fullURL)
    print(r.json())
    return r
