from app.api.features.json_to_sql import convert_json_to_sql_schema
from app.api.features.math_formulas_in_latex import convert_formula_to_latex
from app.api.features.schemas.services_schemas import FormulaToLatexSchema, JsonToSQLSchema, TranslationSchema, XmlToSQLSchema
from app.api.features.translator import translate_text
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

@router.post("/math-formulas-in-latex")
async def submit_tool( data: FormulaToLatexSchema, _ = Depends(key_check)):
    logger.info(f"Args. loaded successfully: {data}")
    logger.info("Generating the Math. Formula in LaTeX...")

    result = convert_formula_to_latex(data)

    logger.info("The Math Formula in LaTeX has been successfully generated")

    return result

@router.post("/translator")
async def submit_tool( data: TranslationSchema, _ = Depends(key_check)):
    logger.info(f"Args. loaded successfully: {data}")
    logger.info(f"Generating the translaton from {data.source_language} to {data.target_language}...")

    result = translate_text(data)

    logger.info("The translation has been successfully generated")

    return result