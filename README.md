# Converter Suite Backend

**Converter Suite Backend** is a robust backend service designed to handle multiple business models for various data transformation needs. It provides efficient and scalable solutions for converting data formats and handling business logic across different domains. The backend supports conversions such as **JSON to SQL**, **XML to SQL**, **Math to LaTeX**, **Translator**, **Info to Table**, and **Image Transcription**. This service utilizes state-of-the-art AI models to ensure high accuracy and precision in its transformations.

Developed by **Wilfredo Aaron Sosa Ramos**, this project leverages cutting-edge technologies such as **FastAPI**, **LangChain**, **Google Generative AI (Multimodal)**, **GPT-4o-mini**, and integrates a **few-shot learning approach** for optimized responses in JSON format.

## Table of Contents

- [1. Features](#1-features)
- [2. Supported Business Models](#2-supported-business-models)
- [3. Technologies Used](#3-technologies-used)
- [4. Few-shot Learning Approach](#4-few-shot-learning-approach)
- [5. API Endpoints](#5-api-endpoints)
- [6. How to Use](#6-how-to-use)

---

## 1. Features

The **Converter Suite Backend** offers comprehensive services that cater to various conversion needs. Its main features include:

- **Data Conversion**: Efficiently handles conversions such as JSON to SQL and XML to SQL, supporting complex queries and database schemas.
- **Math to LaTeX**: Converts mathematical expressions into LaTeX format for academic and professional usage.
- **Translation Services**: Provides multilingual translation support, capable of translating text across a wide variety of languages.
- **Information Extraction**: Converts unstructured information into tabular data for easy integration and analysis.
- **Image Transcription**: Extracts text from images, including complex formats like handwritten text or scanned documents.
- **Multimodal AI Integration**: Supports multimodal inputs and outputs, enabling the handling of a wide range of file types such as PDFs, images, and more.

The backend ensures high performance, accuracy, and scalability, making it ideal for integration into business processes that require precise data handling and transformation.

---

## 2. Supported Business Models

The **Converter Suite Backend** provides six key business models for data transformation and AI-powered services:

- **JSON to SQL**: This service converts JSON input into SQL queries, allowing the creation and manipulation of databases directly from structured JSON data. The system supports multiple SQL dialects such as MySQL, PostgreSQL, and SQLite.

- **XML to SQL**: Similar to the JSON to SQL model, the XML to SQL service converts XML data into SQL statements, ensuring the accurate translation of XML schemas into relational database models.

- **Math to LaTeX**: This service converts complex mathematical expressions into LaTeX code, facilitating the creation of academic papers, presentations, and professional documentation.

- **Translator**: A powerful multilingual translation service that converts text between different languages, leveraging **Google Generative AI** for high-accuracy translations.

- **Info to Table**: This service processes unstructured information and converts it into structured tables. It can be used to extract data from paragraphs, documents, or other unformatted text and display it in a tabular format for easy data management.

- **Image Transcription**: Converts text from images (including complex images such as scanned documents or handwritten notes) into machine-readable text. This service supports various image formats and uses multimodal AI to handle different text recognition challenges.

Each of these business models is optimized for speed and accuracy, allowing businesses to seamlessly integrate data transformation into their workflows.

---

## 3. Technologies Used

The **Converter Suite Backend** leverages a wide range of technologies to provide fast, reliable, and accurate conversions. The primary technologies include:

- **Python**: The backend is built using Python, a highly versatile language for AI and backend development.
  
- **FastAPI**: A modern and high-performance API framework that ensures fast and scalable API services. It supports asynchronous request handling and ensures that the backend can handle a large number of concurrent users.
  
- **LangChain**: A framework designed for developing language models and making them easier to use in various business processes. LangChain facilitates the integration of AI models for tasks such as translation, data extraction, and content generation.

- **Google Generative AI (Multimodal)**: A powerful AI model that handles tasks across text, images, and various data formats. The backend utilizes this model for complex tasks such as image transcription and multimodal input/output handling.

- **GPT-4o-mini**: An optimized version of the GPT-4 model that powers natural language understanding and generation tasks. GPT-4o-mini is used to enhance the backend’s writing services, such as translation and text-to-SQL conversion.

- **Few-shot Learning**: The backend employs few-shot learning to improve accuracy in tasks like data extraction, image transcription, and language translation. This learning technique allows the system to generalize better from limited examples, ensuring robust performance.

These technologies together provide a flexible, scalable, and accurate solution for various business transformation models.

---

## 4. Few-shot Learning Approach

The **Converter Suite Backend** uses a **few-shot learning approach** to optimize its AI-driven transformations. Few-shot learning allows the AI to generalize better across different tasks by training on a small set of examples. This approach improves the performance of several key features:

- **Text-to-SQL Conversions**: The few-shot learning approach ensures that the backend generates accurate SQL queries even from complex or less-structured JSON or XML data.
  
- **Math to LaTeX**: It improves the system’s ability to convert mathematical formulas accurately, even when the input is provided in non-standard or varied formats.

- **Multimodal Data Handling**: Few-shot learning allows the backend to handle a diverse set of inputs, such as images and unstructured text, and process them efficiently.

This approach allows the backend to perform reliably across a wide range of use cases with minimal user input.

---

## 5. API Endpoints

The **Converter Suite Backend** offers several API endpoints to handle different business models. Below is an overview of the key endpoints and their functionality:

- **POST /json-to-sql**: This endpoint converts JSON data into SQL queries. The user provides the JSON data, and the API responds with the corresponding SQL queries based on the database type.

- **POST /xml-to-sql**: Accepts XML input and converts it into SQL statements. The API can handle various database dialects, including MySQL and PostgreSQL.

- **POST /math-formulas-in-latex**: Converts mathematical expressions into LaTeX code. This endpoint is ideal for academic or professional users who need to present complex math formulas.

- **POST /translator**: Accepts text input for multilingual translation. The API responds with the translated text in the desired language.

- **POST /text-to-conceptual-table**: This endpoint processes unstructured text and returns it in a structured table format, making it easier to analyze and work with.

- **POST /image-transcription**: Accepts an image file (e.g., scanned documents or images with text) and transcribes the text within the image. The API supports various image formats and uses advanced text recognition algorithms.

These endpoints allow businesses to easily integrate the backend’s capabilities into their own systems, providing powerful tools for data transformation and conversion.

---

## 6. How to Use

To start using the **Converter Suite Backend**, follow these steps:

1. **Set up the API**: Clone the repository and install the necessary dependencies using the command:

```bash
pip install -r requirements.txt
```

2. **Run the API Server**: Use the following command to run the FastAPI server:
```bash
uvicorn app.main --host 0.0.0.0 --port 8000
```

3. **Access the API**: Once the server is running, you can access the API locally at `http://localhost:8000`. You can send POST requests to the specific endpoints (e.g., `/json-to-sql`, `/translate`) with the required input data.

4. **Multimodal Input**: When using endpoints like `/image-transcription`, you can upload images in various formats such as PNG or JPG, and the API will handle the transcription.

The backend is designed for ease of use and scalability, making it easy to integrate with a variety of business systems and workflows.
