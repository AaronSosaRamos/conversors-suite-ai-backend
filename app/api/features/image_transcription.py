from app.api.features.schemas.services_schemas import ImageTranscriptionSchema
from app.api.logger import setup_logger

from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

logger = setup_logger(__name__)

def image_transcription(data: ImageTranscriptionSchema):
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": "Give me the text transcript of what you see in the image",
            },
            {"type": "image_url", "image_url": data.img_url},
        ]
    )
    response = llm.invoke([message])
    return response