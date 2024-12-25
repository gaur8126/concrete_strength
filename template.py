import os 
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO)

project_name = 'concrete_strength'

list_of_file = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transform.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    "requirements.txt",
    "app.py",
    "setup.py",
    "notebook/EDA.ipynb",
    "notebook/modeltraining.ipynb",
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating dir : {filepath} for the {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)) == 0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"creating emplty file {filepath}")
    else:
        logging.info(f"{filename} is already exists")



