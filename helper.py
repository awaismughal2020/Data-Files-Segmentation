import re


def get_segmentation_from_response(response):
    if isinstance(response, list) and len(response) > 0 and 'text' in response[0]:
        return response[0]['text']
    else:
        return None


def extract_file_type(document_text):
    match = re.search(r'classified as:\s*([^\n]+)', document_text)

    if match:
        classification = match.group(1).strip()
        classification_cleaned = re.sub(r'^\d+\.\s*', '', classification)
        return classification_cleaned
    else:
        return "No valid classification type found."
