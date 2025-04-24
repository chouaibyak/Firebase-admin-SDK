import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()




############################################
#                                          #
#      Dekete data with Firestore          #
#                                          #
############################################

#delete data - known ID
db.collection('persons').document('achraf').delete()

#delete data - known ID - field
db.collection('persons').document('achraf').update({
  "social":firestore.DELETE_FIELD
})

#delete docs - unkown ID 
docs = db.collection('persons').get()
for doc in docs:
  key = doc.id
  db.collection('persons').document(key).delete()
  

