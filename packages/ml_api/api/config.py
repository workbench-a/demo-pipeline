import pathlib
import os

# Set the package root to 
# the parent of the parent of the currrent directory
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

class Config:
  DEBUG = False
  TESTING = False
  SERVER_PORT = 5000


class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class ProductionConfig(Config):
  DEBUG = False
  SERVER_ADDRESS: os.environ.get('SERVER_ADDRESS', '0.0.0.0')
  SERVER_PORT: os.environ.get('SERVER_PORT', '5000')