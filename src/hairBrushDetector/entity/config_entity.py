from pathlib import Path
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    images_path: Path
    labels_path: Path
    dataset_config_path: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file_path: Path
    required_files: list
    
@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    status_file_path: Path
    epochs: int
    image_size: int
    