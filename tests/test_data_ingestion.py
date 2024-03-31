import pytest
from pathlib import Path
import os

def test_data_ingestion():
    file_path=Path('artifacts/data_ingestion/data.csv')
    assert  os.path.exists(file_path)