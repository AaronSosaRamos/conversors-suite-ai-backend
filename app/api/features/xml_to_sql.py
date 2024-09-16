from app.api.features.schemas.services_schemas import XmlToSQLSchema
from app.api.logger import setup_logger

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
load_dotenv(find_dotenv())

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

logger = setup_logger(__name__)

def convert_xml_to_sql_schema(input: XmlToSQLSchema):

  prompt_txt = """
  You are a database schema generation expert. Please analyze the following XML input and generate the corresponding SQL schema for the specified DBMS.

  1. Ensure that all tables have a primary key, specifically an `id` field, and define appropriate foreign key relationships if there are nested elements or collections in the XML.
  2. Generate SQL based on the specific DBMS mentioned, following the syntax and constraints for the specified DBMS (e.g., MySQL, PostgreSQL, SQLite).

  XML Input:
  {xml_input}

  SQL DBMS:
  {sql_dbms}

  Provide a well-formatted SQL script that is ready to be executed in the specified DBMS.
  Only provide the SQL script, nothing else.
  """

  prompt_template = PromptTemplate(
      template=prompt_txt,
      input_variables=["xml_input", "sql_dbms"]
  )

  chain = prompt_template | llm
  result = chain.invoke({"xml_input": input.xml_input, "sql_dbms": input.sql_dbms})
  return result