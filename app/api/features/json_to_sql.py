from app.api.features.schemas.services_schemas import JsonToSQLSchema
from app.api.logger import setup_logger

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
load_dotenv(find_dotenv())

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

logger = setup_logger(__name__)

def convert_json_to_sql_schema(input: JsonToSQLSchema):

  prompt_txt = """
  You are a database schema generation expert. Please analyze the following JSON input and generate the corresponding SQL schema for the specified DBMS.

  1. Ensure that all tables have a primary key, specifically an `id` field, and define appropriate foreign key relationships if there are nested objects or arrays in the JSON.
  2. Generate SQL based on the specific DBMS mentioned, following the syntax and constraints for the specified DBMS (e.g., MySQL, PostgreSQL, SQLite).

  JSON Input:
  {json_input}

  SQL DBMS:
  {sql_dbms}

  Provide a well-formatted SQL script that is ready to be executed in the specified DBMS.
  Only provide the SQL script, nothing else.
  """

  prompt_template = PromptTemplate(
      template=prompt_txt,
      input_variables=["json_input", "sql_dbms"]
  )

  chain = prompt_template | llm
  result = chain.invoke({"json_input": input.json_input, "sql_dbms": input.sql_dbms})

  logger.info(f"Generated SQL Schema: {result}")

  return result