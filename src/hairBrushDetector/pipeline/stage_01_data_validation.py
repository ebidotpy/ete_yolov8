import os
import sys
from hairBrushDetector.config.configuration import ConfigurationManager
from hairBrushDetector.components.data_validation import DataValidation
from hairBrushDetector.logger import logging
from hairBrushDetector.exception import AppException

STAGE_NAME = "data_validation"

class DataValidationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            data_config = config.get_data_ingestion_config()
            validation_config = config.get_data_validation_config()
            
            data_validation = DataValidation(data_config=data_config, validation_config=validation_config)
            data_validation.validat_all_files_exist()
            
        
        except Exception as e:
            raise AppException(e, sys)

try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>>>satge {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx====================================x")

except Exception as e:
    raise AppException(e, sys)
