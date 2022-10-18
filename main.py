import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore_async


def data_base(request):
    # Use the application default credentials.
    cred = credentials.ApplicationDefault()

    firebase_admin.initialize_app(cred)
    db = firestore_async.client()

    async def add_document(doc_ref, new_doc):
        await doc_ref.set(new_doc)

    doc_ref = db.collection("users").document("alovelace")
    new_doc = {"first": "Ada", "last": "Lovelace", "born": 1815}
    add_document(doc_ref, new_doc)

    doc_ref = db.collection("users").document("aturing")
    new_doc = {"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912}
    add_document(doc_ref, new_doc)
