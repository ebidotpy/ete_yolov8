import os
import sys
from pathlib import Path
from hairBrushDetector.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from hairBrushDetector.utils import read_yaml, create_directories
from hairBrushDetector.entity.config_entity import (DataValidationConfig, 
                                                    DataIngestionConfig)
from hairBrushDetector.logger import logging
from hairBrushDetector.exception import AppException

class ConfigurationManager:
    def __init__(self, 
                 config_file_path = CONFIG_FILE_PATH, 
                 params_file_path = PARAMS_FILE_PATH):
        try:
            
            self.config = read_yaml(config_file_path)
            self.params = read_yaml(params_file_path)
        
            create_directories([self.config.root_dir])
    
        except Exception as e:
            raise AppException(e, sys)
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion
            create_directories([config.root_dir])
            
            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir, 
                images_path=config.images_path, 
                labels_path=config.labels_path, 
                dataset_config_path=config.dataset_config_path
            )
            
            return data_ingestion_config
        
        except Exception as e:
            raise AppException(e, sys)
        
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            
            config = self.config.data_validation
            create_directories([config.root_dir])
        
            data_validation_config = DataValidationConfig(
                root_dir=config.root_dir, 
                status_file_path=config.status_file_path, 
                required_files=config.required_files
            )
            
            return data_validation_config
        except Exception as e:
            raise AppException(e, sys)
    
        
        