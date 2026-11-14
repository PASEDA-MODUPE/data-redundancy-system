import boto3
from botocore.exceptions import ClientError
import re

dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1"
)

table = dynamodb.Table("CustomerRecords")


def validate_customer(email, name, phone):

    if not email or not name or not phone:
        return False, "All customer fields are required."

    email = email.strip().lower()
    name = name.strip()
    phone = phone.strip()

    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if not re.match(email_pattern, email):
        return False, "Invalid email address."

    if len(name) < 2:
        return False, "Customer name must contain at least 2 characters."

    phone_pattern = r"^\+?[0-9\s-]{7,20}$"

    if not re.match(phone_pattern, phone):
        return False, "Invalid phone number."

    return True, "Customer details are valid."


def add_customer(email, name, phone):

    valid, message = validate_customer(email, name, phone)

    if not valid:
        return False, message

    email = email.strip().lower()
    name = name.strip()
    phone = phone.strip()

    try:
        table.put_item(
            Item={
                "email": email,
                "name": name,
                "phone": phone
            },
            ConditionExpression="attribute_not_exists(email)"
        )

        return True, "Unique customer record saved."

    except ClientError as error:

        error_code = error.response["Error"]["Code"]

        if error_code == "ConditionalCheckFailedException":
            return False, "Duplicate email address."

        print("Database error:", error)
        return False, "A database error occurred."


print("Customer validation system is ready.")
