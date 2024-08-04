import os 
import logging 
from datetime import datetime as dt

LOG_DIR = "logs"
TIMESTAMP = dt.now().strftime("%d-%m-%Y_%H-%M-%S") 

def get_log_file_name():
    file_name = f"log_{TIMESTAMP}.log"
    return file_name

LOG_FILENAME = get_log_file_name() 

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILENAME)

logging.basicConfig(level=logging.INFO, filemode='w',
                    format='[%(asctime)s] \t%(levelname)s \t%(lineno)d \t%(filename)s \t%(funcName)s \t%(message)s',
                    filename=LOG_FILE_PATH)

logger = logging.getLogger('video_summarizer') 


