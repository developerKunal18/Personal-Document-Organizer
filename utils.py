from datetime import datetime, date
from config import DATE_FORMAT


def get_valid_date(prompt, allow_blank=False):
    while True:
        value = input(prompt).strip()

        if allow_blank and not value:
            return ""

        try:
            parsed_date = datetime.strptime(value, DATE_FORMAT).date()
            return parsed_date.isoformat()
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format.")


def get_document_status(expiry_date):
    if not expiry_date:
        return "No Expiry Date"

    expiry = date.fromisoformat(expiry_date)
    today = date.today()

    if expiry < today:
        return "Expired"

    if expiry == today:
        return "Expires Today"

    return "Valid"


def get_valid_id(prompt):
    while True:
        try:
            document_id = int(input(prompt))

            if document_id <= 0:
                print("ID must be greater than zero.")
                continue

            return document_id

        except ValueError:
            print("Please enter a valid numeric ID.")
