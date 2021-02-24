from google.cloud import firestore
from datetime import date

today = date.today()

db = firestore.Client()
doc_ref = db.collection(u'bq-to-ga').document(str(today))
doc_ref.set({
    u'status': u'success',
})

# Then query for documents
users_ref = db.collection(u'bq-to-ga')

for doc in users_ref.stream():
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
