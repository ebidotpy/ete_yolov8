import sys
from hairBrushDetector.logger import logging
from hairBrushDetector.exception import AppException
from hairBrushDetector.pipeline.stage_01_data_validation import DataValidationPipeline
from hairBrushDetector.pipeline.stage_02_training_pipeline import TrainingPipeline

STAGE_NAME = "Data Validation"

try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>>>satge {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx====================================x")

except Exception as e:
    raise AppException(e, sys)


STAGE_NAME = "Model Training"

try:
    if __name__ == "__main__":
        logging.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<\n\nx=========================x")

except Exception as e:
    raise AppException(e, sys)