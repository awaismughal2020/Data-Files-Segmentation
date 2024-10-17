# Document Classification Service

This repository contains code for automatically classifying documents into predefined categories using AWS Bedrock's machine learning services.

## Overview

This project leverages AWS Bedrock to classify document content into one of the following categories:

1. Curriculum Vitae
2. Personal Profile
3. Educational Background
4. Passport
5. Identification Card
6. Other

It uses a pre-defined model to analyze document content, segment it based on major headlines and titles, and return the document's classification.

## Files

### 1. `main.py`
This is the main file that handles document segmentation and classification. It does the following:

- Reads the content of a document.
- Uses AWS Bedrock to classify the document content into one of the categories listed above.
- Prints the result of the classification.

### 2. `helper.py`
Contains utility functions to:
- Extract the file type based on the segmentation response from the Bedrock model.
- Parse and extract the relevant information from the Bedrock response.

### 3. `readFile.py`
Handles reading the document content from the file.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/document-classification.git
    cd document-classification
    ```

2. Install dependencies:
    ```bash
    pip install boto3
    ```

3. Set up AWS credentials by configuring the AWS CLI or using environment variables:
    ```bash
    export AWS_ACCESS_KEY_ID=your-access-key
    export AWS_SECRET_ACCESS_KEY=your-secret-key
    export AWS_REGION_NAME=your-region
    ```

4. Set the following environment variables for the Bedrock and Anthropic versions:
    ```bash
    export BEDROCK_SEARCH_MODEL_ID=your-bedrock-model-id
    export BEDROCK_REGION_NAME=your-region-name
    export ANTHROPIC_VERSION=your-anthropic-version
    ```

## Usage

1. Place the document you want to classify inside the `tempDir/` directory.

2. Run the script:
    ```bash
    python main.py
    ```

3. The classification result will be printed in the console.

## Example

Suppose you have a file `testing.txt` containing a resume or CV. After running the script, the result might be:
```
This document is classified as: Curriculum Vitae
```

## Error Handling

If an error occurs during the Bedrock model invocation, the script will catch and print the error to the console.

## License

This project is licensed under the MIT License.

