from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()


def create_app(*, config_object) -> Flask:
  """"""
  flask_app = Flask('ml_api')

  flask_app.config.from_object(config_object)
  flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  # Initialize plugins
  db.init_app(flask_app)
  ma.init_app(flask_app)

  with flask_app.app_context():
    # Include our routes
    from api.routes.ml import ml
    from api.routes.app import app
    from api.routes.tweet import tweet
    # from api import routes
    flask_app.register_blueprint(app)
    flask_app.register_blueprint(ml)
    flask_app.register_blueprint(tweet)

    db.create_all()

  return flask_app