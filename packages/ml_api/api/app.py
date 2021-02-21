from flask import Flask

def create_app(*, config_object) -> Flask:
  """"""
  flask_app = Flask('ml_api')
  flask_app.config.from_object(config_object)

  from api.controller import ml_app
  flask_app.register_blueprint(ml_app)

  return flask_app