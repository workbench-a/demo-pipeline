from flask import jsonify
from api.data.models.tweets import Tweet, TweetSchema
from api.app import db
import json

# Init schema
tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)

# Populate database table from file
def json_to_table(file_path):
    """"""
    # try:
    json_array = json.load(open(file_path))
    for item in json_array:
        # id = item['id']
        tweet_id = item['tweet_id']
        name = item['name']
        text = item['text']
        tweet_created = item['tweet_created']
        user_timezone = item['user_timezone']

        new_tweet = Tweet(tweet_id, name, text, tweet_created, user_timezone)
        db.session.add(new_tweet)
    db.session.commit()
    return '<h1>Records Added<h1>', 200
    # except:
    #   return '<h1>Load Failed</h1>', 500

# Create a Tweet
def create_one(request):
  """"""
    try:
        tweet_id = item['tweet_id']
        name = item['name']
        text = item['text']
        tweet_created = item['tweet_created']
        user_timezone = item['user_timezone']

        new_tweet = Tweet(name, description, price, qty)

        db.session.add(new_tweet)
        db.session.commit()

        return tweet_schema.jsonify(new_tweet), 200
    except:
        return '<h1>Record Creation Failed</h1>', 500

def read_all(request):
  """"""
    try:
        all_tweets = Tweet.query.all()
        result = tweets_schema.dump(all_tweets)
        return jsonify(result), 200
    except:
        return '<h1>Read All Failed</h1>', 500

def read_by_id(request, id):
  """"""
    try:
        tweet = Tweet.query.get(id)
        return tweet_schema.jsonify(tweet), 200
    except:
        return '<h1>Read By Id Failed</h1>', 500

def update_by_id(request, id):
  """"""
    try:
        tweet = Tweet.query.get(id)

        id = request.json['id']
        tweet_id = request.json['tweet_id']
        name = request.json['name']
        text = request.json['text']
        tweet_created = request.json['tweet_created']
        user_timezone = request.json['user_timezone']

        tweet.tweet_id = tweet_id
        tweet.name = name
        tweet.text = text
        tweet.tweet_created = tweet_created 
        tweet.user_timezone = user_timezone

        db.session.commit()
        return tweet_schema.jsonify(tweet), 200
    except:
        return '<h1>Update By Id Failed</h1>', 500

def delete_by_id(request, id):
  """"""
    try:
        tweet = Tweet.query.get(id)
        db.session.delete(tweet)
        db.session.commit()

        return tweet_schema.jsonify(tweet), 200
    except:
        return '<h1>Delete By Id Failed</h1>', 500
