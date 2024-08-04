import logging 
import os 

from from_root import from_root 
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"  

log_dir = 'logs'

logs_path = os.path.join(from_root(),log_dir,LOG_FILE) 

os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(level=logging.DEBUG,
                    filename=logs_path,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)