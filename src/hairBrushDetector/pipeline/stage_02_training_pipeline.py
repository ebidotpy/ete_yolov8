import os
import sys
from pathlib import Path
from hairBrushDetector.logger import logging
from hairBrushDetector.exception import AppException
from hairBrushDetector.components.training import Training
from hairBrushDetector.config.configuration import ConfigurationManager

STAGE_NAME = "training_pipeline"

class TrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_training_config()
            validation_config = config.get_data_validation_config()
            data_config = config.get_data_ingestion_config()
            training_pipeline = Training(training_config=training_config, validation_config=validation_config, data_config=data_config)
            training_pipeline.training()
        except Exception as e:
            raise AppException(e, sys)

try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<\n\nx=========================x")

except Exception as e:
    raise AppException(e, sys)