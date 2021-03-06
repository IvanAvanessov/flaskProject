from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)


class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomID = db.Column(db.String(10), index=True, unique=True)
    createdTime = db.Column(db.DateTime)
    lastUpdatedTime = db.Column(db.DateTime)
    currentUsers = db.Column(db.Integer)
    roomTableName = db.Column(db.String(100), unique=True)


def create_room_model(room_name):
    class Room(db.Model):
        __tablename__ = room_name
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(100))
        messageTime = db.Column(db.DateTime)
        message = db.Column(db.Text)

        def to_dict(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    return Room


def create_roomUsers_model(Room):
    class RoomUsers(db.Model):
        __tablename__ = Room.__tablename__ + '_users'
        pass
