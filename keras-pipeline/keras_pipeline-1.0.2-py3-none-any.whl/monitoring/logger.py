# TODO

import logging

logger = logging.getLogger("pipeline")
logger.setLevel(logging.INFO)

fh = logging.FileHandler("output.log")
ch = logging.StreamHandler()

logger.addHandler(fh)
logger.addHandler(ch)

logger.info("Hello world!")


import logging

# Loggers have hierachial structure, so when you get "pipeline.XYZ", 
# you inherit all settings from "pipeline" logger.
logger = logging.getLogger("pipeline.FeatureSelection")

class FeatureSelection:
  def __init__(self):
    logger.info("Creating FeatureSelection")