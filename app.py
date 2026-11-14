import boto3
import re
from botocore.exceptions import ClientError

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


def normalize_phone(phone):
    return re.sub(r"[\s-]", "", phone)


def add_customer(email, name, phone):

    valid, message = validate_customer(email, name, phone)

    if not valid:
        return False, message

    email = email.strip().lower()
    name = name.strip()
    phone = normalize_phone(phone)

    try:
        # Check whether the email already exists.
        existing_email = table.get_item(
            Key={"email": email},
            ConsistentRead=True
        )

        if "Item" in existing_email:
            return False, "Duplicate email address."

        # Check whether the phone number already exists.
        existing_records = table.scan(
            FilterExpression="#phone = :phone",
            ExpressionAttributeNames={
                "#phone": "phone"
            },
            ExpressionAttributeValues={
                ":phone": phone
            },
            ConsistentRead=True
        )

        if existing_records.get("Items"):
            return False, "Duplicate phone number."

        # Save the new customer only if both checks pass.
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
