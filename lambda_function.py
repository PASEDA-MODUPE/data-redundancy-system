import json
from app import add_customer

def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "")

    if method == "OPTIONS":
        return {
            "statusCode": 200,
            "body": ""
        }

    if method != "POST":
        return {
            "statusCode": 405,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"success": False, "message": "Method not allowed."})
        }

    try:
        data = json.loads(event.get("body") or "{}")
    except (json.JSONDecodeError, TypeError):
        data = {}

    success, message = add_customer(
        data.get("email", ""),
        data.get("name", ""),
        data.get("phone", "")
    )

    status = 201 if success else (409 if message == "Duplicate email address." else 400)

    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"success": success, "message": message})
    }
