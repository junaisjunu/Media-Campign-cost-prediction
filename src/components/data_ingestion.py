import gdown
from src.utils.common import create_directories
from src.excption.exception import customexception
import sys
from src import logger
from src.entity.config_entity import DataIngestionConfig


class DataIgestion:
    def __init__(self,config: DataIngestionConfig) -> None:
        self.config=config

    def downlaod_data(self):
        try:
            # data_url=self.config.data_url
            g_url='https://drive.google.com/uc?id='
            id=self.config.data_url.split('/')[-2]
            data_url=g_url+id
            data_path=self.config.data_path
            directory_path=self.config.data_ingestion_root
            create_directories([directory_path])
            gdown.download(data_url,data_path)
            logger.info(f"data downlaoded successfully")

        except Exception as e :
            raise customexception(e,sys)

        
