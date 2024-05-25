import os
from text_summarizer.logger import logger
from text_summarizer.config import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = False
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion"))

            for file in self.config.ALL_REQUIRED_FILES:
                if file not in all_files:
                    validation_status = False
                    logger.warning(f"{file} is missing from the Data Ingestion")
                    break
                else:
                    validation_status=True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation Status: {validation_status}")
            
            return validation_status
        
        except Exception as e:
            raise e