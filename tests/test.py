from src.utils.common import read_yaml
from pathlib import Path

content=read_yaml(Path('config\config.yaml'))
print(content.name)