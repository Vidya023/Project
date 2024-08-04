import os
from pathlib import Path  

project_name = 'pneumonia' 

list_of_files = [
    f'{project_name}/__init__.py',
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/exception/__init__.py', 
    f'{project_name}/logger/__init__.py',
    'app.py',
    'requirements.txt',
    'setup.py',
    'notebook/model.ipynb',
    'templates/index.html'     
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