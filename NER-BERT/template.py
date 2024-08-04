import os
from pathlib import Path  

project_name = 'nlp_files' 

list_of_files = [
    f'{project_name}/__init__.py',
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/data_ingestion.py',
    f'{project_name}/components/data_validation.py',
    f'{project_name}/components/data_transformation.py',
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/components/model_evaluation.py',
    f'{project_name}/components/model_pusher.py',
    f'{project_name}/configuration/__init__.py',
    f'{project_name}/configuration/s3_operations.py',
    f'{project_name}/constants/__init__.py',
    f'{project_name}/entity/__init__.py',
    f'{project_name}/entity/artifact_entity.py',
    f'{project_name}/entity/config_entity.py',
    f'{project_name}/exception/__init__.py', 
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/pipeline/training_pipeline.py',
    f'{project_name}/pipeline/prediction_pipeline.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/utils/main_utils.py',
    f'{project_name}/data_access/__init__.py',
    'notebook/EDA.ipynb',
    'notebook/model_select.ipynb',
    'notebook/mongodb.ipynb',
    'app.py',
    'requirements.txt',
    'Dockerfile',
    '.dockerignore',
    'demo.py',
    'setup.py',
    'config/model.yaml',
    'config/schema.yaml'    
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)   # to create directory
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:   # to create file in directory, opening a writeable file and pass 
            pass
    else:
        print(f'File exists at {filepath}')         
    