import pandas as pd
from sklearn.model_selection import train_test_split
from src.excption.exception import customexception
import sys
from src import logger
from src.utils.common import create_directories
from src.entity.config_entity import DataTransformationConfig
import os

class DataTransformation:
    def __init__(self,data_txm_config:DataTransformationConfig) -> None:
        self.config=data_txm_config

    

        

    def data_transformation_for_training(self):
        try:
            logger.info(f"Data transformation has started")
            data=pd.read_csv(self.config.data_path)
            data=self.get_basic_transfomed_data(data)
            train,test = train_test_split(data, test_size=0.3, random_state=42)
            logger.info(f"train data shape{train.shape} and test data shape {test.shape}")
            create_directories([self.config.data_transformation_root])
            train.to_csv(os.path.join(self.config.data_transformation_root,'train.csv'),index=False)
            test.to_csv(os.path.join(self.config.data_transformation_root,'test.csv'),index=False)
            logger.info(f"data transformation completed successfully!")
        except Exception as e:
            raise customexception(e,sys)

    
    def data_transforamtion_for_prediction(self,data :pd.DataFrame):
        data=self.get_basic_transfomed_data(data)
        return data
    
    @staticmethod
    def get_basic_transfomed_data(data: pd.DataFrame):
        if 'id' in data.columns:
            data=data.drop('id',axis=1)
        data=data.dropna()
        data=data.drop_duplicates()
        return data






