from text_summarizer.pipeline import DataIngestionTrainingPipeline, DataValidationTrainingPipeline, DataTransformationTrainingPipeline, ModelTrainerPipeline, ModelEvaluationPipeline
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
    logger.info(f"========= {STAGE_NAME} started =========")
    data_validation = DataValidationTrainingPipeline()
    status = data_validation.main()
    if status:
        logger.info(f"========= {STAGE_NAME}  completed =========")
    else:
        logger.warning(f"XXXXXXXXX {STAGE_NAME} incompleted XXXXXXXXX")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation"
try:
    logger.info(f"========= {STAGE_NAME} started =========")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"========= {STAGE_NAME}  completed =========")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f"========= {STAGE_NAME} started =========")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"========= {STAGE_NAME}  completed =========")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"========= {STAGE_NAME} started =========")
    model_trainer = ModelEvaluationPipeline()
    model_trainer.main()
    logger.info(f"========= {STAGE_NAME}  completed =========")
except Exception as e:
    logger.exception(e)
    raise e