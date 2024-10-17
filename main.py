import os
import boto3
import json
from helper import extract_file_type, get_segmentation_from_response
from readFile import read_document


def document_segmentation(document_content):
    print("\nDocument segmentation function initiated...\n\n")
    model_id = os.getenv('BEDROCK_SEARCH_MODEL_ID')

    messages = [
        {
            "role": "user",
            "content": f"""Based on the content below, classify it into one of the following categories:
            1. Curriculum vitae
            2. Personal Profile
            3. Educational Background
            4. Passport
            5. Identification Card
            6. Other

            consider document major headlines and titles

            Document content:
            {document_content}

            Please classify this document, just give the classification type dont give reasons. Answer it as 'this document is classified as: '"""
        }
    ]

    anthropic_version = os.getenv('ANTHROPIC_VERSION')

    try:
        client = boto3.client(
            service_name='bedrock-runtime',
            region_name=os.getenv("BEDROCK_REGION_NAME")
        )

        payload = {
            "anthropic_version": anthropic_version,
            "max_tokens": 100,
            "messages": messages
        }

        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(payload),
            contentType='application/json'
        )

        response_body = json.loads(response['body'].read().decode('utf-8'))
        if 'content' in response_body:
            return extract_file_type(get_segmentation_from_response(response_body['content']))

        return None
    except Exception as e:
        print(f"Error during model invocation: {e}")
        return None



if __name__ == '__main__':
    document_content = read_document('tempDir/testing.txt')
    print(document_segmentation(document_content))