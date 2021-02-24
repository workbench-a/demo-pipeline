from flask import Blueprint, request, jsonify
from api.controllers.tweet import create_one, read_all, \
		read_by_id, update_by_id, delete_by_id, json_to_table
from api.config import PACKAGE_ROOT

tweet = Blueprint('tweet', __name__)

# Add records from file
@tweet.route('/tweet/add_records_from_file', methods=['GET'])
def add_records_from_file():
    """Create table of tweets from local json file.
    """
    file_path = PACKAGE_ROOT / "api" / "data" / "lake" / "test" / "airline_tweets.json"
    return json_to_table(file_path)


# Create a Tweet
@tweet.route('/tweet', methods=['POST'])
def add_tweet():
	"""Add tweet to database.
	"""
    return create_one(request)

# Get All Tweets
@tweet.route('/tweets', methods=['GET'])
def get_tweets():
	"""Read tweet from database.
	"""
    return read_all(request)

# Get Single Tweets
@tweet.route('/tweet/<id>', methods=['GET'])
def get_tweet(id):
	"""Read tweet by id from database.
	"""
    return read_by_id(request, id)

# Update a Tweet
@tweet.route('/tweet/<id>', methods=['PATCH'])
def update_tweet(id):
	"""Update tweet by id.
	"""
    return update_by_id(request, id)

# Delete Tweet
@tweet.route('/tweet/<id>', methods=['DELETE'])
def delete_tweet(id):
	"""Delete tweet by id.
	"""
    return delete_by_id(request, id)