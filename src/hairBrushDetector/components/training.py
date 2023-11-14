import os
from ultralytics import YOLO
import sys
from pathlib import Path
from hairBrushDetector.utils import read_yaml
from hairBrushDetector.logger import logging
from hairBrushDetector.exception import AppException
from hairBrushDetector.entity.config_entity import (TrainingConfig, 
                                                    DataValidationConfig, 
                                                    DataIngestionConfig)

class Training:
    def __init__(self, 
                 training_config: TrainingConfig, 
                 validation_config: DataValidationConfig, 
                 data_config: DataIngestionConfig):
        try:
            self.trining_config = training_config
            self.validation_config = validation_config
            self.data_config = data_config
        
        except Exception as e:
            raise AppException(e, sys)
    def check_data_validation(self):
        try:
            status = read_yaml(Path(self.validation_config.status_file_path))
            return status.Validation_status

        
        except Exception as e:
            raise AppException(e, sys)
    def training(self):
        try:
            if self.check_data_validation():
                
                os.system(f"yolo detect train data={self.data_config.dataset_config_path} project={self.trining_config.root_dir} epochs={self.trining_config.epochs} imgsz={self.trining_config.image_size}")
            else:
                logging.info("data validation rejected, please check your data folder")
            
        except Exception as e:
            raise AppException(e, sys)