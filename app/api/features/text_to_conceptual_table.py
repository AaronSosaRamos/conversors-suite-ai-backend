from app.api.features.schemas.services_schemas import InfoToTableSchema
from app.api.logger import setup_logger

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
load_dotenv(find_dotenv())

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

logger = setup_logger(__name__)

def convert_info_to_conceptual_table(input: InfoToTableSchema):
    prompt_txt = """
    You are an expert in organizing information into clear and concise tables. Please analyze the following paragraph and extract key concepts, organizing them into a well-structured table format.

    1. Create appropriate column headers based on the concepts presented in the text.
    2. Organize the information into rows, grouping similar ideas together for clarity.

    Paragraph:
    {text_input}

    Context (if any):
    {context}

    Provide only the table in the markdown format, nothing else.
    """

    prompt_template = PromptTemplate(
        template=prompt_txt,
        input_variables=["text_input", "context"]
    )

    chain = prompt_template | llm
    result = chain.invoke({
        "text_input": input.text_input,
        "context": input.context
    })

    return result