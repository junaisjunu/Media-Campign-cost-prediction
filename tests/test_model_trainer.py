import pytest
from pathlib import Path
import os

def test_model_trainer():
    file_path=Path('artifacts/model_trainer/model.pkl')
    assert  os.path.exists(file_path)