from text_summarizer.pipeline import DataIngestionTrainingPipeline
from text_summarizer.logger import logger

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"========= stage {STAGE_NAME} started =========")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"========= stage {STAGE_NAME} completed =========")
except Exception as e:
    logger.exception(e)
    raise e