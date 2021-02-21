from flask import Blueprint, request, jsonify
from ml_demo import __version__ as _version
from api import __version__ as api_version

ml_app = Blueprint('ml_api', __name__)

@ml_app.route("/health", methods=['GET'])
def health():
  """"""
  return '<h1>Health Status: ok<h1>'

@ml_app.route('/version', methods=['GET'])
def version():
  """"""
  if request.method == 'GET':
    return jsonify({'model_version': _version,
                    'api_version': api_version})
@ml_app.route('/v0/demo_classify/demo_classifier', methods=['POST'])
def demo_classify_text():
  """"""
  if request.method == 'POST':
    # Do stuff
    return jsonify({'a_data_point': 'a_sentiment'})