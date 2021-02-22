from api.app import db
from api.app import flask_app
import api.data.models

with flask_app.test_request_context():
     db.init_app(app)

     db.create_all()