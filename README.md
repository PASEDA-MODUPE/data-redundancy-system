# Data Redundancy Removal System

## Project Overview
A cloud-based customer registration system that validates customer details and checks for duplicate email addresses and phone numbers before saving records.

## Project Objectives
- Validate customer information.
- Prevent duplicate email registrations.
- Detect existing phone numbers.
- Store customer records in a cloud database.
- Improve customer data accuracy.

## Architecture

Customer Registration Website
        |
        v
GitHub Pages
        |
        v
AWS Lambda Function URL
        |
        v
AWS Lambda (Python)
        |
        v
Amazon DynamoDB

## AWS Services Used

- AWS Lambda: Runs the backend application.
- Amazon DynamoDB: Stores customer records.
- AWS IAM: Controls permissions between services.
- Lambda Function URL: Provides an HTTP endpoint for the website.

## Technologies
- Python
- JavaScript
- HTML
- CSS
- Boto3
- Git and GitHub

## Website
https://paseda-modupe.github.io/data-redundancy-system/

## GitHub Repository
https://github.com/PASEDA-MODUPE/data-redundancy-system

## Current Features
- Customer registration form.
- Email validation.
- Name validation.
- Phone number validation.
- Duplicate email detection.
- Duplicate phone number detection.
- Cloud database storage.
- Website connected to AWS Lambda.

## Known Limitations
- Phone-number duplicate detection currently uses a DynamoDB scan and is not an atomic uniqueness guarantee.
- Matching the same person using different email addresses and different phone numbers is not implemented.
- Advanced false-positive detection is not implemented.
- The public Lambda Function URL currently has no authentication. It should be secured before production use.

## Deployment
The frontend is hosted on GitHub Pages. The backend runs on AWS Lambda and stores customer records in Amazon DynamoDB.

## Learning Outcome
This project provided practical experience with serverless computing, cloud databases, IAM permissions, Python development, API integration, and cloud deployment.
