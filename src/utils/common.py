
from box import ConfigBox
from pathlib import Path
from src.excption.exception import customexception
import sys
import yaml
from src import logger


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as f:
            content=yaml.safe_load(f)
            logger.info(f"file loaded succesfully from the path {path_to_yaml}")
            return ConfigBox( content)
    except Exception as e:
        raise customexception(e,sys)
