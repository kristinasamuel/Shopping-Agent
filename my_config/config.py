from agents import AsyncOpenAI,OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
import requests
from agent.run import RunConfig

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if  not gemini_api_key:
    raise ValueError("Gemini api key is not set")

externel_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "GEMINI_BASE_PATH"

)

model = OpenAIChatCompletionsModel(
    model = "GEMINI_MODEL_NAME",
    openai_client = externel_client
)

config = RunConfig(
    model = model,
    model_provider = externel_client,
    tracing_disabled = True
)
