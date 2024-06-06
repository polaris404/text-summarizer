# Text Summarization

>**Notes:** 
>* This project focuses mainly on End to End implementation rather than the accuracy of the Model. I've reduced the actual training dataset to about 10-20% as my device cannot handle this huge dataset.
>* You can change the dataset used for training in <br>
`text-summarizer/text_summarizer/components/model_training`
>* I've not hosted the model on AWS as the it requires huge amount of resources like RAM and GPU which is not affordable for me. 

## Introduction
An NLP application that summarizes the text provided as an input. It uses Google's pegasus model for summarization which is trained on various news articles. Checkout the model [here](https://huggingface.co/google/pegasus-cnn_dailymail). The dataset that has been used for training is Samsung's [samsum](https://huggingface.co/datasets/Samsung/samsum) dataset. 


## Workflow

The components of the project are as follows:
1. **Data Ingestion and Validation:** First we collect the data from the source and store it locally. After that we check if all the necessary files are present or not. As I'm directly loading dataset from the HuggingFace library, I skipped most part of this step but if we get dataset from other sources like github we need to implement this step thoroughly.
2. **Data Tranformation:** In this step we transfer the data to feed into our model. As this is a NLP task, we tokenized the dataset using `transformers` library, after that we create appropriate features for our dataset.
3. **Model Training:** Now we import necessary model required for our task, in this case it is [pegasus](https://huggingface.co/google/pegasus-cnn_dailymail) by Google. We use the parameters stored in `params.yaml` file. We can find the appropriate parameters while training and evaluaitng in IPython Notebook. Then we feed in the transformed dataset that we saved locally and start training.
4. **Model Evaluation:** Once the training is complete we evaluate our model using certain metrics like rouge_score etc. and once we are satisfied we are ready for the next step.
5. **Prediction:** As the name suggests, in this step we provide input to the model in the form of text and we get summary as an output.

Each of the components mentioned follow the workflow mentioned:
* **Configuration:** We set up a config file name `config.yaml` in the root directory of the project which contains the configuration required in each step of the project. We also setup an sub-module inside project module with name `entity` which helps us to maintain proper return types of the configuration data and `config` which convert data from `config.yaml` to appropriate configuration class. 
* **Component:** Here we setup the whole functionality of each step (except Prediction) using the configuration data. This is sub-module inside the project module.
* **Pipeline:** Now we setup a pipeline for each step that involves getting configuration and passing it to appropriate component.
* **Modifying `main.py`:** After the pipeline is being setup, we add the pipeline to this file. Once all the piplines are created we import them into the file and run them in the proper order.

> For user interface, I've implemented a localhost server using FastAPI and set routes for training and giving input to the model.
