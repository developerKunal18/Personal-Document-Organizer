from storage import load_documents, save_documents
from utils import get_document_status


def add_document(title, category, document_number, issue_date,
                 expiry_date, file_location, notes):
    documents = load_documents()

    document_id = max(
        [document["id"] for document in documents],
        default=0
    ) + 1

    document = {
        "id": document_id,
        "title": title,
        "category": category,
        "document_number": document_number,
        "issue_date": issue_date,
        "expiry_date": expiry_date,
        "file_location": file_location,
        "notes": notes
    }

    documents.append(document)
    save_documents(documents)

    print("\nDocument added successfully!")


def view_documents():
    documents = load_documents()

    if not documents:
        print("\nNo documents found.")
        return

    print("\n" + "-" * 110)
    print(
        f"{'ID':<5} {'Title':<22} {'Category':<18} "
        f"{'Issue Date':<15} {'Expiry Date':<15} {'Status':<15}"
    )
    print("-" * 110)

    for document in documents:
        status = get_document_status(document["expiry_date"])
        expiry_date = document["expiry_date"] or "N/A"
        issue_date = document["issue_date"] or "N/A"

        print(
            f"{document['id']:<5} "
            f"{document['title'][:21]:<22} "
            f"{document['category'][:17]:<18} "
            f"{issue_date:<15} "
            f"{expiry_date:<15} "
            f"{status:<15}"
        )

    print("-" * 110)


def search_documents(keyword):
    documents = load_documents()
    keyword = keyword.lower()

    results = [
        document for document in documents
        if keyword in document["title"].lower()
        or keyword in document["category"].lower()
        or keyword in document["document_number"].lower()
    ]

    display_search_results(results)


def filter_by_category(category):
    documents = load_documents()

    results = [
        document for document in documents
        if document["category"].lower() == category.lower()
    ]

    display_search_results(results)


def display_search_results(results):
    if not results:
        print("\nNo matching documents found.")
        return

    print("\nMatching Documents:")

    for document in results:
        print(
            f"\nID: {document['id']}"
            f"\nTitle: {document['title']}"
            f"\nCategory: {document['category']}"
            f"\nDocument Number: {document['document_number'] or 'N/A'}"
            f"\nIssue Date: {document['issue_date'] or 'N/A'}"
            f"\nExpiry Date: {document['expiry_date'] or 'N/A'}"
            f"\nStatus: {get_document_status(document['expiry_date'])}"
            f"\nFile Location: {document['file_location'] or 'N/A'}"
            f"\nNotes: {document['notes'] or 'N/A'}"
        )


def update_document(document_id, title, category, document_number,
                    issue_date, expiry_date, file_location, notes):
    documents = load_documents()

    for document in documents:
        if document["id"] == document_id:
            document["title"] = title
            document["category"] = category
            document["document_number"] = document_number
            document["issue_date"] = issue_date
            document["expiry_date"] = expiry_date
            document["file_location"] = file_location
            document["notes"] = notes

            save_documents(documents)
            print("\nDocument updated successfully!")
            return

    print("\nDocument ID not found.")


def delete_document(document_id):
    documents = load_documents()

    updated_documents = [
        document for document in documents
        if document["id"] != document_id
    ]

    if len(updated_documents) == len(documents):
        print("\nDocument ID not found.")
        return

    save_documents(updated_documents)
    print("\nDocument deleted successfully.")
