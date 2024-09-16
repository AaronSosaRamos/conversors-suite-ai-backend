from app.api.features.schemas.services_schemas import FormulaToLatexSchema
from app.api.logger import setup_logger

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
load_dotenv(find_dotenv())

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

logger = setup_logger(__name__)

def convert_formula_to_latex(input: FormulaToLatexSchema):
    prompt_txt = """
    You are a mathematical expert. Please analyze the following mathematical formula input and convert it into a well-formatted LaTeX equation.

    Formula Input:
    {formula_input}

    Provide only the LaTeX code, nothing else.
    """

    prompt_template = PromptTemplate(
        template=prompt_txt,
        input_variables=["formula_input"]
    )

    chain = prompt_template | llm
    result = chain.invoke({"formula_input": input.formula_input})

    return result