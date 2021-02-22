from flask import jsonify
from ml_demo import __version__ as _version
from api import __version__ as api_version

def get_health():
  """"""
  return '<h1>ML Health Status: ok<h1>'

def get_version(request):
  """"""
  if request.method == 'GET':
    return jsonify({'model_version': _version,
                    'api_version': api_version})

def classify_text(request):
  """"""
  if request.method == 'POST':
      # Do stuff
      return jsonify({'a_data_point': 'a_sentiment'})