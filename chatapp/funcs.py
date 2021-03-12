import string, random
from datetime import datetime
from .models import Rooms, create_room_model
from main import db

roomIDTableNameLength = 8
roomIDLength = 6


def create_room() -> str:
    missing = ''
    while missing is not None:
        letters = string.ascii_uppercase
        roomID = ''.join(random.choice(letters) for i in range(roomIDLength))
        createdTime = datetime.now()
        lastUpdatedTime = datetime.now()
        currentUsers = 0
        letters = string.ascii_letters
        roomTableName = roomID + '_' + ''.join(random.choice(letters) for i in range(roomIDTableNameLength))

        missing = Rooms.query.filter_by(roomID=roomID)
        if missing is None:
            db.create_all()
            db.session.commit()
            newRoom = Rooms(roomID=roomID, createdTime=createdTime, lastUpdatedTime=lastUpdatedTime,
                            currentUsers=currentUsers,
                            roomTableName=roomTableName)
            db.session.add(newRoom)
            _ = create_room_model(roomTableName)
            db.create_all()
            db.session.commit()
            return roomID
    return None
