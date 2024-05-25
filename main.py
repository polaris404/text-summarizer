from text_summarizer.pipeline import DataIngestionTrainingPipeline
from text_summarizer.pipeline import DataValidationTrainingPipeline
from text_summarizer.logger import logger

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"========= {STAGE_NAME} started =========")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"========= {STAGE_NAME}  completed =========")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation"
try:
    logger.info(f"========= Data Validation started =========")
    data_validation = DataValidationTrainingPipeline()
    status = data_validation.main()
    if status:
        logger.info(f"========= Data Validation completed =========")
    else:
        logger.warning(f"XXXXXXXXX Data Validation incompleted XXXXXXXXX")
except Exception as e:
    logger.exception(e)
    raise e