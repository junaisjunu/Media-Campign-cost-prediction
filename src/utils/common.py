
from box import ConfigBox
from pathlib import Path
from src.excption.exception import customexception
import sys
import yaml
from src import logger
from ensure import ensure_annotations
import os
import json

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as f:
            content=yaml.safe_load(f)
            logger.info(f"file loaded succesfully from the path {path_to_yaml}")
            return ConfigBox( content)
    except Exception as e:
        raise customexception(e,sys)
    
@ensure_annotations
def create_directories(paths : list):
    try:
        for path in paths:
            os.makedirs(path,exist_ok=True)
    except Exception as e:
        raise customexception(e,sys)


@ensure_annotations
def save_json(path : Path, data : dict):
    try:
        with open(path,"w") as f:
            json.dump(data,f,indent=4)
        logger.info(f"json file save successfully at {path}")
    except Exception as e:
        raise customexception(e,sys)
    
def load_json(path: Path)-> ConfigBox:
    with open(path,"r") as f:
        content=json.load(f)
        logger.info(f"json file loaded successfully from {path}")
        return ConfigBox(content)

