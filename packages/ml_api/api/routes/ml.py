"""Routes for machine learning model predictions.
"""
from flask import Blueprint, request, jsonify
from api.controllers.ml import get_health, get_version, classify_text, predict

ml = Blueprint('ml', __name__)

@ml.route("/ml/health", methods=['GET'])
def health():
    """ Check that api is online.
    """
    return get_health()

@ml.route('/ml/version', methods=['GET'])
def version():
    """Get api and model versions.
    """
    return get_version(request)

@ml.route('/v0/demo_classify/text_classifier', methods=['POST'])
def demo_classify_text():
    """Classify request data with demo_model.
    """
    return classify_text(request)

@ml.route('/v0/predict/regression_demo', methods=['GET', 'POST'])
def demo_predict():
    """Classify request data with demo_model.
    """
    return predict()
