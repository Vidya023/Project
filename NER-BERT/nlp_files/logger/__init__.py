import logging 
import os 

from nlp_files.constants import *

logs_path = os.path.join(os.getcwd(),"logs",TIMESTAMP) 

os.makedirs(logs_path, exist_ok = True) 

LOG_FILE_PATH = os.path.join(logs_path, LOGS_FILE_NAME) 

logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILE_PATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)