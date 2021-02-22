import pathlib
import os
from dotenv import load_dotenv

# Set the package root to the parent of the parent of the currrent directory
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

# Set the environment path to ./.env
env_path = PACKAGE_ROOT / '.env'
load_dotenv(dotenv_path=env_path)

# Database uri
DATABASE_ENGINE = os.environ.get('DATABASE_ENGINE')
DATABASE_PATH = pathlib.Path(__file__).resolve() / 'api' / 'data' / 'databases' / os.environ.get('DATABASE_PATH')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_ADDRESS = os.environ.get('DATABASE_ADDRESS')

# # Make Database URI
# def make_uri(db_engine='SQLITE', db_name='temp_db', db_user='', db_password='', db_address=''):
#   """"""
#   uri_string = {
#     'SQLITE': f'sqlite:///{db_name}',
#     'POSGRESQL': f'postgresql+psychopg2://{db_user}:{db_password}@{db_address}/{db_name}',
#     'MYSQL': f"mysql+pymysql://{db_user}:{db_password}@{db_address}/{db_name}",
#   }
#   if db_engine == 'SQLITE':
#     return uri_string[db_engine].format(db_name)
#   elif db_engine == 'POSGRESQL':
#     return uri_string[db_engine].format(db_user, db_password, db_address, db_name)
#   elif db_engine == 'MYSQL':
#     return uri_string[db_engine].format(db_user, db_password, db_address, db_name)

# Flask app config

class Config:
  DEBUG = False
  TESTING = False
  SERVER_PORT = 5000

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class ProductionConfig(Config):
  # SQLALCHEMY_DATABASE_URI = make_uri(DATABASE_ENGINE, DATABASE_PATH, DATABASE_USER, DATABASE_PASSWORD, DATABASE_ADDRESS)
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
  DEBUG = False
  SERVER_ADDRESS: os.environ.get('SERVER_ADDRESS', '0.0.0.0')
  SERVER_PORT: os.environ.get('SERVER_PORT', '5000')