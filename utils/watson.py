import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

api_key = os.getenv("API_KEY")
project_id = os.getenv("PROJ_ID")
space_id = os.getenv("SPACE_ID")

credentials = Credentials(
    url="https://us-south.ml.cloud.ibm.com",
    api_key=api_key
)

model_id = "ibm/granite-3-8b-instruct"
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 200,
    "min_new_tokens": 0,
    "repetition_penalty": 1
}

model = ModelInference(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id,
    space_id=space_id
)