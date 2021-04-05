from flask import Flask
import random
import string

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

app = Flask(__name__)
app.config.from_object(config.DevConfig)
app.url_map.strict_slashes = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from chatapp.views import chatapp_url

app.register_blueprint(chatapp_url, url_prefix='/')

from ccyapp.views import ccyapp_url
app.register_blueprint(ccyapp_url, url_prefix='/ccy')

if __name__ == '__main__':
    app.run(port=8000)
