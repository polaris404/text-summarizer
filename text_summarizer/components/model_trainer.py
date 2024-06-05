from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from text_summarizer.logger import logger
import torch
import os

from text_summarizer.config import ModelTrainerConfig
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        logger.info(f'--------Device: {device}--------')
        tokenizer = AutoTokenizer.from_pretrained(self.config.model)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model).to(device)

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))

        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        dataset_pt = load_from_disk(self.config.data_path)
        train_test_split = dataset_pt['train'].train_test_split(test_size=0.1)
        train_subset = train_test_split['train']

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=train_subset, 
                  eval_dataset=dataset_pt["validation"])
        
        trainer.train()

        ## Save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))