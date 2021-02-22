from api.app import db
from api.app import ma

# Tweet Class/Model
class Tweet(db.Model):
  """"""
  
  __tablename__ = 'tweet'
  id = db.Column(db.Integer, primary_key=True)
  tweet_id = db.Column(db.Integer) 
  name = db.Column(db.String(100))
  text = db.Column(db.String(300))
  tweet_created = db.Column(db.String(50))
  user_timezone = db.Column(db.String(50))

  def __init__(self, tweet_id, name, text, tweet_created, user_timezone):
    self.tweet_id = tweet_id
    self.name = name
    self.text = text
    self.tweet_created = tweet_created
    self.user_timezone = user_timezone

# Tweet Schema
class TweetSchema(ma.Schema):
  class Meta:
    fields = ('id', 'tweet_id', 'name', 'text', 'tweet_created', 'user_timezone')