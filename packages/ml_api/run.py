from api.app import create_app
from api.config import DevelopmentConfig, ProductionConfig, MODEL_DEVELOPMENT

if MODEL_DEVELOPMENT:
  from api.config import MODEL_PATHS
  import sys
  for path in MODEL_PATHS:
    sys.path.append(path)

application = create_app(config_object=ProductionConfig)

if __name__ == '__main__':
  application.run()