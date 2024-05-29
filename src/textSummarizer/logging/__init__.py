import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" #this gives logging history. it will create on file and the time and the label name
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log") #creates the directory
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  # it will create the file and log it 
        logging.StreamHandler(sys.stdout) #create the log in terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger")