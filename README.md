# Data Redundancy Removal System

## 1. Project Overview

The Data Redundancy Removal System is a cloud-based application designed to validate customer information and prevent duplicate records from being stored in a database.

## 2. Project Objectives

- Validate customer information before saving.
- Reject invalid email addresses.
- Reject invalid phone numbers.
- Prevent duplicate customer email addresses.
- Store valid and unique customer records in AWS DynamoDB.

## 3. Technologies Used

- Python: Application programming language.
- Boto3: AWS SDK for Python.
- Amazon DynamoDB: Cloud NoSQL database.
- AWS CloudShell: Environment used to run the application.

## 4. How the System Works

1. A customer record is submitted.
2. Python validates the customer's email, name and phone number.
3. Invalid information is rejected.
4. The application checks whether the email already exists.
5. Duplicate records are rejected.
6. Valid and unique records are saved in DynamoDB.

## 5. AWS Services

Amazon DynamoDB stores customer records.

AWS CloudShell provides the terminal environment for running the Python application.

## 6. Current Test Results

- Valid customer records were saved successfully.
- Duplicate email addresses were rejected.
- Invalid email addresses were rejected.
- Empty customer names were rejected.
- Invalid phone numbers were rejected.
- Three valid customer records were confirmed in DynamoDB.

## 7. Current Limitation

The system currently detects duplicates using email addresses. It does not yet identify the same person using different email addresses.

## 8. Future Improvements

- Add stronger duplicate detection.
- Build a simple user interface.
- Improve customer identity verification.
- Add monitoring and reporting.

## 9. Azure Comparison

- Amazon DynamoDB is comparable in purpose to Azure Cosmos DB.
- AWS CloudShell is comparable to Azure Cloud Shell.
- Boto3 is comparable to the Azure SDK for Python.

These services have similar purposes but different configurations and APIs.

## 10. Project Status

Working prototype with customer validation, duplicate email prevention and DynamoDB storage.
