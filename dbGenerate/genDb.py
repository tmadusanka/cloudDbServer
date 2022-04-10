import os
import json
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore DB
cred = credentials.Certificate('newkey.json')
default_app = initialize_app(cred)
db = firestore.client()

def createDb( dbName , infile , listTag):
    users_ref = db.collection(dbName)

    # Opening JSON file
    f = open(infile,)

    data = json.load(f)

    for i in data[listTag]:
        print(i)
        users_ref.add(i)

def cleanDb(dbName):
    docs = db.collection(dbName).get() # Get all data
    for doc in docs:
        key = doc.id
        db.collection(dbName).document(key).delete()

def create_user_db():
    createDb('users' , 'user_data.json', 'users')
    
def create_company_db():
    createDb('company' , 'company_data.json', 'companies')

def create_vendor_db():
    createDb('vendor' , 'vendor_data.json', 'vendors')

def create_service_db():
    createDb('service' , 'service_data.json', 'services')

if __name__ == "__main__":
    cleanDb('users')
    cleanDb('company')
    cleanDb('vendor')
    cleanDb('service')

    create_user_db()
    create_company_db()
    create_vendor_db()
    create_service_db()




