import pytest
from src import logger
import logging
import os
from datetime import datetime

def test_log_directory_creation():
    log_dir = "logs"
    assert os.path.exists(log_dir)



    
def test_logging_format(caplog):
    caplog.set_level(logging.INFO)
    logger.info("Test message")
    assert caplog.records[0].message == "Test message"


