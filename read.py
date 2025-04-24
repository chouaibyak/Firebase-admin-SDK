import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()




############################################
#                                          #
#      Reading data with Firestore         #
#                                          #
############################################

#getting a document with a known ID
result = db.collection('persons').document('achraf').get()
if result.exists:
  print(result.to_dict())

#get  all documents in a collection
docs = db.collection('persons').get()
for doc in docs:
  print(doc.to_dict())

# Querying
docs = db.collection('persons').where("age", "==", 10).get()
for doc in docs:
  print(doc.to_dict())

docs = db.collection('persons').where("social", "array_contains", "youtub").get()
for doc in docs:
  print(doc.to_dict())

docs = db.collection('persons').where("address", "in", ["london", "milan"]).get()
for doc in docs:
  print(doc.to_dict())