from flask import jsonify
from api import __version__ as api_version
from flask import Blueprint, request, jsonify

# Model imports
from demo_model.processing.data_management import load_dataset
from demo_model.predict import make_prediction
from demo_model import __version__ as _version

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

def predict():
    if request.method == 'GET':
        # Step 1: load data
        input_data = load_dataset(mode="production", file_name="test.csv")
        # Step 2: make prediction
        result = make_prediction(input_data=input_data)
        # Step 3: Convert prediction result from numpy ndarray to list
        predictions = result.get('predictions').tolist()
        # Step 4: Get prediction meta-data
        version = result.get('version')
        errors = ''
        # Step 5: Return all results as JSON
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})
    elif request.method == 'POST':
      return '<h1>POST prediction endpoint</h1>'
        # # Step 1: Extract POST data from request body as JSON
        # if 'file' not in request.files:
        #   return jsonifyI('File not found'), 400
        
        # file = request.files['file']


        # # Step 2: Basic file extension validation
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)

        #     # Step 3: Save the file
        #     # Note, in production, this would require careful
        #     # validation, management and clean up.
        #     file.save(os.path.join(UPLOAD_FOLDER, filename))

        #     _logger.debug(f'Inputs: {filename}')

        #     # Step 4: perform prediction
        #     result = make_single_prediction(
        #         image_name=filename,
        #         image_directory=UPLOAD_FOLDER)

        #     _logger.debug(f'Outputs: {result}')

        # readable_predictions = result.get('readable_predictions')
        # version = result.get('version')

        # # Step 5: Return the response as JSON
        # return jsonify(
        #     {'readable_predictions': readable_predictions[0],
        #      'version': version})
                  