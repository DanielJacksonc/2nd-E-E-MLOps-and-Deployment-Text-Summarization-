#Instead of creating different folder amd files manually, we use this code to create all the folders and files in one go.
#STEP 1:
#IMPORT ALL NEEDE LIBRARY
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] %(message)s:]')

#STEP 2
#ASSIGN A VARIABLE FOR PROJECT NAME

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  #this contains the folders and file
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/_utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile", #for deployment
    "requirements.txt", #conatining all requirements
    "setup.py",  #FOR Packet setup
    "research/trials.ipynb", #will contain all notebook experiments
]


#STEP 3
#CREATE A FUNCTION THAT WILL CREATE FOLDERS AND FILES
for filepath in list_of_files:  #looping through this list of files
    filepath = Path(filepath) #file path pass to path function. it first determines the os you are using. IT GIVES YOU ALL THE PATH ONE BY ONE.
    filedir, filename = os.path.split(filepath)  #it will return file directoy and file name.

       #check if the file directory is empty or not
    if filedir != "": #this means if the file directory is not empty
        os.makedirs(filedir, exist_ok=True)  #if the file directory is not empty, it will create the directory. exist_ok=True
        logging.info(f"Creating directory:{filedir} for the file {filename}") #it will create the directory and log it.

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #if the file is not exists or file size is 0, it will create the file.
        with open(filepath,'w') as f: #write the file
            pass
            logging.info(f"Creating empty file: {filepath}") #it will create the file and log it.


    
    else:
        logging.info(f"{filename} is already exists") #if the file is already exists, it will log it.