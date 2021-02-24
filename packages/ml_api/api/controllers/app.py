from flask import jsonify
# from ml_demo import __version__ as _version
from api import __version__ as api_version

def get_health():
  """"""
    return '<h1> Health Status: ok<h1>'

def get_version(request):
  """"""
    if request.method == 'GET':
       return jsonify({'api_version': api_version})