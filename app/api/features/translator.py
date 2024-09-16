from app.api.features.schemas.services_schemas import TranslationSchema
from app.api.logger import setup_logger

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
load_dotenv(find_dotenv())

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

logger = setup_logger(__name__)

def translate_text(input: TranslationSchema):
    prompt_txt = """
    You are a language expert. Please translate the following text from {source_language} to {target_language}.

    Text to translate:
    {text_input}

    Provide only the translated text, nothing else.
    """

    prompt_template = PromptTemplate(
        template=prompt_txt,
        input_variables=["text_input", "source_language", "target_language"]
    )

    chain = prompt_template | llm
    result = chain.invoke({
        "text_input": input.text_input,
        "source_language": input.source_language,
        "target_language": input.target_language
    })

    return result