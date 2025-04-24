import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()




############################################
#                                          #
#      Update data with Firestore          #
#                                          #
############################################

#update data - known key
db.collection('persons').document('achraf').update({'age':50})
db.collection('persons').document('achraf').update({
  "social": firestore.ArrayRemove['youtube']
})
db.collection('persons').document('achraf').update({
  "social": firestore.ArrayUnion['youtube']
})

#update data - unknown key
docs = db.collection('persons').get()
for doc in docs:
  if doc.to_dict()['age'] > 10:
    key = doc.id
    db.collection('persons').document(key).update({
      "agegroup": "middle age"
    })