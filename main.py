# Develop a Shopping Agent utilizing the OpenAI Agents 
# Import necessary libraries and modules
from agents import Agent ,Runner ,AsyncOpenAI , OpenAIChatCompletionsModel ,RunConfig
from dotenv import load_dotenv
import os
import requests
import re
import chainlit as cl

# Load environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Raise error if API key is not found
if  not gemini_api_key:
    raise ValueError("Gemini api key is not set")

# Set up external openai client with Gemini API
externel_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

)

# Define the model configuration using Gemini key
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = externel_client
)

# Configure how the agent will run
config = RunConfig(
    model = model,
    model_provider = externel_client,
    tracing_disabled = True
)

# Function to fetch and filter products based on user keywords
def searched_product(keyword:str) :
    try:
        url = "https://hackathon-apis.vercel.app/api/products"
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()

        words = re.findall(r"\b\w+\b",keyword.lower())
        stopwords = {"the","with","under","above","for","of","and","or","a","an","in","to","below","between","is","best"}
        keywords = [w for w in words if w not in stopwords ]

        filtered = []
        for p in products:
            title = p.get("title","").lower()
            price = p.get("price",None)
            if not title or price is None:
                continue
            if any(kw in title for kw in keywords ):
                filtered.append(f".{p['title']} | Rs {price}")
        if filtered:
            return "\n".join(filtered[:5])
        else :
            return ""

    except  Exception as e:
        return f"API Error: {str(e)}"


# # Chainlit: When chat starts
@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hi! I'm your Shopping Assistant 🤖.How may I assist you with your shopping needs today?").send()

# Chainlit: When a new message is received
@cl.on_message
async def main(message: cl.Message):
    user_question = message.content

    # Create a shopping assistant agent
    agent = Agent(
        name="Shopping Assistant",
        instructions="You are a helpful shopping assistant that answers product-related questions",
        model=model
    )
     
     # Run the agent and get the response
    result = await Runner.run(agent, user_question)
    final_output = result.final_output

    # Search for matching products
    product_results = searched_product(user_question)

    # Send the assistant's response and product matches
    await cl.Message(
        content=f"**🔍 Matching Products:**\n{product_results}\n\n** Assistant's Answer:**\n{final_output}"
    ).send()
