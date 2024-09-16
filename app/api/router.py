from app.api.features.json_to_sql import convert_json_to_sql_schema
from app.api.features.schemas.services_schemas import JsonToSQLSchema, XmlToSQLSchema
from app.api.features.xml_to_sql import convert_xml_to_sql_schema
from fastapi import APIRouter, Depends
from app.api.logger import setup_logger
from app.api.auth.auth import key_check

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

logger = setup_logger(__name__)
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/json-to-sql")
async def submit_tool( data: JsonToSQLSchema, _ = Depends(key_check)):
    logger.info(f"Args. loaded successfully: {data}")
    logger.info("Generating the SQL Schema from the JSON data...")

    result = convert_json_to_sql_schema(data)

    logger.info("The SQL schema has been successfully generated")

    return result

@router.post("/xml-to-sql")
async def submit_tool( data: XmlToSQLSchema, _ = Depends(key_check)):
    logger.info(f"Args. loaded successfully: {data}")
    logger.info("Generating the SQL Schema from the XML data...")

    result = convert_xml_to_sql_schema(data)

    logger.info("The SQL schema has been successfully generated")

    return result