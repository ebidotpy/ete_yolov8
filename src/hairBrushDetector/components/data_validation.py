import os
import sys
from hairBrushDetector.logger import logging
from hairBrushDetector.exception import AppException
from hairBrushDetector.utils import create_directories
from hairBrushDetector.entity.config_entity import (DataValidationConfig, 
                                                    DataIngestionConfig)

class DataValidation:
    def __init__(self, data_config: DataValidationConfig, validation_config: DataIngestionConfig):
        try:
            self.data_config = data_config
            self.validation_config = validation_config
        except Exception as e:
            raise AppException(e, sys)
        
    def validat_all_files_exist(self) -> bool:
        try:
            validation_satus = None
            
            all_files = os.listdir(str(self.data_config.root_dir))
            # all_files = [self.data_config.images_path, self.data_config.labels_path, self.data_config.dataset_config_path]
            for file in all_files:
                if file not in self.validation_config.required_files:
                    validation_satus=False
                    create_directories([self.validation_config.root_dir])
                    with open(self.validation_config.status_file_path, "w") as f:
                        f.write(f"Validation status: {validation_satus}")
                else:
                    validation_satus=True
                    create_directories([self.validation_config.root_dir])
                    with open(self.validation_config.status_file_path, "w") as f:
                        f.write(f"Validation status: {validation_satus}")
                    
                    
            
        except Exception as e:
            raise AppException(e, sys)