from flask import Blueprint, request, jsonify
from api.controllers.app import get_health, get_version

app = Blueprint('app', __name__)

@app.route("/health", methods=['GET'])
def health():
  """"""
  return get_health()

@app.route('/version', methods=['GET'])
def version():
  """"""
  return get_version(request)