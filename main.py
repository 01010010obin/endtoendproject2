from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.components.data_validation import DataValidation

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig) 
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info(">>>>>>>>>>>> Data ingestion completed <<<<<<<<<<<<<<")

        logging.info("Initiate Data Validation")
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)

        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info(">>>>>>>>>>>> Data Validation completed <<<<<<<<<<<<<<")
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)


