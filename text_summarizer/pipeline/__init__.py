from text_summarizer.config import ConfigurationManager
from text_summarizer.components.data_ingestion import DataIngestion
from text_summarizer.components.data_validation import DataValidation


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip()
        except Exception as e:
            raise e

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            return data_validation.validate_all_files_exist()
        except Exception as e:
            raise e