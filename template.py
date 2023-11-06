import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "hairBrushDetector"

list_of_files = [
    ".github/workflows/.gitkeeep", 
    "data/.gitkeep", 
    f"{project_name}/components/__init__.py", 
    f"{project_name}/constants/__init__.py", 
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/training_pipline/__init__.py",
    f"{project_name}/constants/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/constants/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trials.ipynb", 
    "app.py", 
    "Dockerfile", 
    "requirements.txt", 
    "setup.py"
]

for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creationg empty file: {filename}")
    else:
        logging.info(f"{filename} is already created")
        