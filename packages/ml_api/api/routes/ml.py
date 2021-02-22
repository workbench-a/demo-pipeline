from flask import Blueprint, request, jsonify
from api.controllers.ml import get_health, get_version, classify_text

ml = Blueprint('ml', __name__)

@ml.route("/ml/health", methods=['GET'])
def health():
  """"""
  return get_health()

@ml.route('/ml/version', methods=['GET'])
def version():
  """"""
  return get_version(request)

@ml.route('/v0/demo_classify/demo_classifier', methods=['POST'])
def demo_classify_text():
  """"""
  return classify_text(request)

@ml.route('/v0/predict/regression', methods=['GET', 'POST'])
def demo_predict():
  """"""
  return make_single_prediction()