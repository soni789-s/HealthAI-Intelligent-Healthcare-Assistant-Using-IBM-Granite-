import os
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning import APIClient
from dotenv import load_dotenv
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams


load_dotenv()

wml_credentials = {
    "apikey": os.getenv("IBM_APIKEY"),
    "url": "https://us-south.ml.cloud.ibm.com"
}

client = APIClient(wml_credentials)
project_id = os.getenv("IBM_PROJECT_ID")
client.set.default_project(project_id)

generate_params = {
            GenParams.MAX_NEW_TOKENS: 2000,
            GenParams.TEMPERATURE:0.7,
            GenParams.STOP_SEQUENCES: ["\nUser question:", "\nQuestion:"]

        }

model = Model(
    model_id="ibm/granite-3-3-8b-instruct",
    credentials=wml_credentials,
    project_id=project_id,
    params=generate_params
)

def query_granite(prompt: str) -> str:
    try:
        response = model.generate(prompt)
        return response['results'][0]['generated_text'].strip()
    except Exception as e:
        return f"\u274c Granite AI Error: {e}"
