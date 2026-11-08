from datetime import date

from storage import initialize_storage
from document_manager import (
    add_document,
    view_documents,
    search_documents,
    filter_by_category,
    update_document,
    delete_document
)
from utils import get_valid_date, get_valid_id


def display_menu():
    print("\n========== PERSONAL DOCUMENT ORGANIZER ==========")
    print("1. Add Document")
    print("2. View All Documents")
    print("3. Search Document")
    print("4. Filter by Category")
    print("5. Update Document")
    print("6. Delete Document")
    print("7. Exit")
    print("=================================================")


def get_document_details():
    title = input("Enter document title: ").strip()
    category = input("Enter category: ").strip()
    document_number = input("Enter document number: ").strip()

    issue_date = get_valid_date(
        "Enter issue date (YYYY-MM-DD, blank if unavailable): ",
        allow_blank=True
    )

    expiry_date = get_valid_date(
        "Enter expiry date (YYYY-MM-DD, blank if no expiry): ",
        allow_blank=True
    )

    if issue_date and expiry_date and expiry_date < issue_date:
        print("Expiry date cannot be before issue date.")
        return None

    file_location = input("Enter file location or path: ").strip()
    notes = input("Enter notes: ").strip()

    if not title or not category:
        print("Document title and category are required.")
        return None

    return (
        title,
        category,
        document_number,
        issue_date,
        expiry_date,
        file_location,
        notes
    )


def main():
    initialize_storage()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            details = get_document_details()

            if details:
                add_document(*details)

        elif choice == "2":
            view_documents()

        elif choice == "3":
            keyword = input(
                "Enter title, category, or document number: "
            ).strip()

            search_documents(keyword)

        elif choice == "4":
            category = input("Enter category: ").strip()
            filter_by_category(category)

        elif choice == "5":
            document_id = get_valid_id(
                "Enter document ID to update: "
            )

            details = get_document_details()

            if details:
                update_document(document_id, *details)

        elif choice == "6":
            document_id = get_valid_id(
                "Enter document ID to delete: "
            )

            delete_document(document_id)

        elif choice == "7":
            print("Thank you for using Personal Document Organizer!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
