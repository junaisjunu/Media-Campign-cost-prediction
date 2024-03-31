from src.constants import *
from src.utils.common import read_yaml,create_directories
from src.entity.config_entity import DataIngestionConfig,DataTransformationConfig

class Configuration:
    def __init__(self,config_path=CONFIG_FILE_PATH
                      ,params_path=PARAMS_FILE_PATH
                      ,schema_path=SCHEMA_FILE_PATH) -> None:
        self.config=read_yaml(config_path)
        self.params=read_yaml(params_path)
        self.schema=read_yaml(schema_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion
        data_ingestion_config=DataIngestionConfig(
                            data_ingestion_root=config.data_ingestion_root,
                            data_url=config.data_url,
                            data_path=config.data_path
                            )
        
        return data_ingestion_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config=self.config.data_transformation
        data_txm_config=DataTransformationConfig(
            data_transformation_root=config.data_transformation_root,
            data_path=config.data_path,
            # transformed_data_path=config.transformed_data_path
            # target=config.target
        )

        return data_txm_config


        