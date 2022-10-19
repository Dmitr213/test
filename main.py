import os

import flask


def hello_world(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    return "Hello World!"


# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore_async
#
#
# def data_base(request):
#     # Use the application default credentials.
#     cred = credentials.ApplicationDefault()
#
#     firebase_admin.initialize_app(cred)
#     db = firestore_async.client()
#
#     async def add_document(doc_ref, new_doc):
#         await doc_ref.set(new_doc)
#
#     doc_ref = db.collection("users").document("alovelace")
#     new_doc = {"first": "Ada", "last": "Lovelace", "born": 1815}
#     add_document(doc_ref, new_doc)
#
#     doc_ref = db.collection("users").document("aturing")
#     new_doc = {"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912}
#     add_document(doc_ref, new_doc)
