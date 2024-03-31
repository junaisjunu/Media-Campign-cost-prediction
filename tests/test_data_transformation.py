import pytest
from pathlib import Path
import os

def test_data_transformation():
    file_path=Path('artifacts/data_transformation/train.csv')
    assert  os.path.exists(file_path)