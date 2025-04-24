import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


############################################
#                                          #
#      Creating data with Firestore        #
#                                          #
############################################


#add documents
data = {
  'name': 'achraf',
  'age': 16,
  'employed':True
  }
db.collection('persons').add(data)

#set documents with known IDs
data = {
  'name': 'achraf',
  'age': 16,
  'employed':True
  }
db.collection('persons').document('achraf').set(data)

#set document with auto IDs
db.collection('persons').document().set(data)

#mergin
db.collection('persons').document('achraf').set({'address': 'london'}, merge=True)

#collection in collection
db.collection('persons').document('achraf').collection('movies').add({
  'name':'vikings',
  'ep':10,
})
