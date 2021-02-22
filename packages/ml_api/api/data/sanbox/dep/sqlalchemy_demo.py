"""
database url is dialect+driver://username:password@db_address/db_name
"""

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# join the inputs into a complete database url.
url = f"mysql+pymysql://{db_user}:{db_pass}@{db_addr}/{db_name}"

# db_address: localhost:5432
DB_ENGINE = {
  SQLITE: f'sqlite:///{db_name}',
  POSGRESQL: f'postgresql+psychopg2://{db_user}}:{db_password}@{db_address}/{db_name}',
  MYSQL: f"mysql+pymysql://{db_user}:{db_password}@{db_address}/{db_name}"
}

def make_db_uri(*, db_type='SQLITE', db_name='temp_db', db_user='user', db_password='password', db_address='localhost:5432'):
  """"""
  if DB_ENGINE == 'SQLITE':
    return DB_ENGINE[db_type].format(DB=db_name)
  elif DB_ENGINE == 'POSGRESQL':
    return DB_ENGINE[db_type].format(db_user, db_password, db_address, db_name=db_name)
  elif DB_ENGINE == 'MYSQL':
    return DB_ENGINE[db_type].format(db_user, db_password, db_address, db_name=db_name)
  
def create_db(*, db_uri='sqlite:///test.db', ):
  """"""
  if not database_exists(engine.url):
    # if the database does not exist, create it
    create_database(engine.url)
  else:
    # If the database exists, connect to it
    engine.connect()

def create_tweet_table(db_uri='sqlite:///test.db'):
  """"""
  from sqlalchemy import Table, Column, Integer, String, MetaData
  engine = create_engine(db_uri, echo = False)
  meta = MetaData()

  students = Table('test_tweets', meta, 
    Column('id', Integer, primary_key = True), 
    Column('body', String(300)), 
  )
  meta.create_all(engine)

def delete_tweet_table(engine):
  """"""
  User.__table__.drop(engine)

def create_tweet_row():
  """"""
  pass

def find():
  """"""
  pass

def update():
  """"""
  pass

def delete():
  """"""
  pass
