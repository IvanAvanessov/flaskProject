from flask import Flask
import random
import string

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config


app = Flask(__name__, static_folder='chatapp/static')
app.config.from_object(config.DevConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from chatapp.views import chatapp_url
app.register_blueprint(chatapp_url, url_prefix='/')


@app.route('/room/<roomID>/', methods=['GET', 'POST'])
def open_room(roomID):
    return 'You are entering room: %s' % roomID


if __name__ == '__main__':
    app.run(port=8000)





