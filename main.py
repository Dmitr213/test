from flask import escape
import functions_framework

@functions_framework.http
def hello_http2(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))


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
