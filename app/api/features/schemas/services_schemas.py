from pydantic import BaseModel, Field

class JsonToSQLSchema(BaseModel):
    json_input: str = Field(..., description="The input JSON string containing the data structure to be converted into SQL.")
    sql_dbms: str = Field(..., description="The type of SQL DBMS for which the SQL script will be generated (e.g., MySQL, PostgreSQL, SQLite).")

class XmlToSQLSchema(BaseModel):
    xml_input: str = Field(..., description="The input XML string containing the data structure to be converted into SQL.")
    sql_dbms: str = Field(..., description="The type of SQL DBMS for which the SQL script will be generated (e.g., MySQL, PostgreSQL, SQLite).")

class FormulaToLatexSchema(BaseModel):
    formula_input: str = Field(..., description="The input string containing the mathematical formula to be converted into LaTeX.")