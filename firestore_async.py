import asyncio
import firebase_admin
from firebase_admin import firestore_async

app = firebase_admin.initialize_app()
db = firestore_async.client()


async def change_db_handler(request):

    try:
        doc_ref = db.collection("users").document("alovelace")
        await doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
        return "Database has been successfully changed"
    except Exception as error:
        return "Error in 'change_db_handler': " + str(error)


def change_db(request):
    return asyncio.run(change_db_handler(request))
