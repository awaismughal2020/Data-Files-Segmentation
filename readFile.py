import os
import PyPDF2
import docx
import pandas as pd
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import boto3
import json



def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def read_pdf_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            content = ''
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    content += text
                else:
                    content += f"\n[Page {page_num + 1}: No extractable text]\n"
        return content
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return None


def read_scanned_pdf_file(file_path):
    try:
        images = convert_from_path(file_path)
        content = ''

        for i, image in enumerate(images):
            text = pytesseract.image_to_string(image)
            if text.strip():
                content += f"\n[Page {i + 1} Scanned Text]:\n{text}\n"
            else:
                content += f"\n[Page {i + 1}]: No extractable text or scanned content.\n"

        return content
    except Exception as e:
        print(f"Error reading scanned PDF: {e}")
        return None


def read_docx_file(file_path):
    doc = docx.Document(file_path)
    content = []
    for paragraph in doc.paragraphs:
        content.append(paragraph.text)
    return '\n'.join(content)


def read_excel_file(file_path):
    df = pd.read_excel(file_path)
    return df.to_string()



def read_document(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == '.txt':
        return read_text_file(file_path)
    elif ext == '.pdf':
        content = read_pdf_file(file_path)
        if "[Page" in content and "No extractable text" in content:
            scanned_content = read_scanned_pdf_file(file_path)
            if scanned_content:
                content += "\n[Scanned PDF content]:\n" + scanned_content
        return content
    elif ext == '.docx':
        return read_docx_file(file_path)
    elif ext == '.xlsx' or ext == '.csv':
        return process_csv_or_xlsx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def format_dataframe_content(df):
    content = ""
    max_rows = 500

    for index, row in df.head(max_rows).iterrows():
        row_content = " | ".join([f"{col}: {str(val)}" for col, val in row.items()])
        content += f"Row {index + 1}: {row_content}\n"

    return content


def process_csv_or_xlsx(file_path):
    ext = os.path.splitext(file_path)[-1].lower()

    try:
        if ext == '.xlsx':
            df = pd.read_excel(file_path)
        elif ext == '.csv':
            df = pd.read_csv(file_path)
        else:
            raise ValueError(f"Unsupported file type for processing: {ext}")

        formatted_content = format_dataframe_content(df)
        return formatted_content

    except Exception as e:
        print(f"Error processing CSV/XLSX file: {e}")
        return None
