import sys,os
from sensor.logger import logging
from sensor.exception import SensorException
import pandas as pd 
from sensor.utils import get_collection_as_dataframe
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity import config_entity
from datetime import datetime
def test_logger_and_exception():
     try:
          logging.info("Starting the test_logger_and_exception")
          result = 3/0
          print(result)
          logging.info("Stopping the test_logger_and_exception")          
     except Exception as e:
          logging.debug("Stopping the test_logger_and_exception")
          raise SensorException(e,sys)


if __name__=="__main__":
     try:
          training_pipeline_config= config_entity.TrainingPipelineConfig()
          data_ingestion_config= DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
     except Exception as e:
          print(e)
