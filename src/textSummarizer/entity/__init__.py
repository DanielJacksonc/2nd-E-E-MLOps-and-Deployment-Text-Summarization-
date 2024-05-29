from dataclasses import dataclass
from pathlib import Path


#FOR DATA INGESTION
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
  
  
  
  
  #FOR DATA VALIDATION  
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path  #the path to the root
    STATUS_FILE: str #the data type of the file
    ALL_REQUIRED_FILES: list #a list of all the required files