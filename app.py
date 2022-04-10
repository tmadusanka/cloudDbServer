import os
import random
import string
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('newkey.json')
default_app = initialize_app(cred)
db = firestore.client()

company_ref = db.collection('company')
users_ref = db.collection('users')
vendor_ref = db.collection('vendor')
service_ref = db.collection('service')
order_ref = db.collection('order')

def getRandomKey():
    letters = string.ascii_letters
    key = ''.join(random.choice(letters) for i in range(20))
    return key

#####################################################################################

@app.route('/login', methods=['GET'])
def login():
    """
        login() : Login and get access key
        Ensure you pass a email and password
        e.g. json={'email': 'email@e1.com', 'password': 'e1234'}
    """
    try:
        email = request.args.get('email')
        password = request.args.get('password')
        docs = users_ref.where("email", "==" , email).get()
        if len(docs) == 1 :
            d = docs[0].to_dict()
            if d['password'] == password :
                return jsonify({"success": True, "data" : d}), 200
            else :
                return jsonify({"success": False, "msg" : "Invalid password"}), 200
        else :
            return jsonify({"success": False, "msg" : "Invalid email"}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/getCompanyForAdmin', methods=['GET'])
def getCompanyForAdmin():
    """
        getCompanyForAdmin() : Get company details for given company admin
        Ensure you user id 
        e.g. json={'user': '<admin id>' }
    """
    try:
        user = request.args.get('user')
        docs = company_ref.where("adminList" , "array_contains" , user).get()
        if len(docs) == 1 :
            d = docs[0].to_dict()
            return jsonify({"success": True, "data" : d}), 200
        else :
            return jsonify({"success": False, "msg" : "Invalid user id"}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/getCompanyForEmployee', methods=['GET'])
def getCompanyForEmployee():
    """
        getCompanyForEmployee() : Get company details for given company emplyee
        Ensure you user id 
        e.g. json={'user': '<employee id>' }
    """
    try:
        user = request.args.get('user')
        docs = company_ref.where("employeeList" , "array_contains" , user).get()
        if len(docs) == 1 :
            d = docs[0].to_dict()
            return jsonify({"success": True, "data" : d}), 200
        else :
            return jsonify({"success": False, "msg" : "Invalid user id"}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/getVendorForAdmin', methods=['GET'])
def getVendorForAdmin():
    """
        getCompanyForEmployee() : Get venodr details for given admin
        Ensure you user id 
        e.g. json={'user': '<vendor id>' }
    """
    try:
        user = request.args.get('user')
        docs = vendor_ref.where("adminList" , "array_contains" , user).get()
        if len(docs) == 1 :
            d = docs[0].to_dict()
            return jsonify({"success": True, "data" : d}), 200
        else :
            return jsonify({"success": False, "msg" : "Invalid user id"}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
@app.route('/getCompany', methods=['GET'])
def getCompany():
    """
        getCompany() : Get company details
        Ensure you user id and company id
        e.g. json={'user': '<user id>' , 'id': '<company id>'}
    """
    try:
        user = request.args.get('user')
        companyId = request.args.get('id')
        docs = company_ref.where("id", "==" , companyId).get()
        if len(docs) == 1 :
            d = docs[0].to_dict()
            return jsonify({"success": True, "data" : d}), 200
        else :
            return jsonify({"success": False, "msg" : "Invalid company id"}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/getVendor', methods=['GET'])
def getVendor():
    """
        getVendor() : Get vendor details
        Ensure you user id and vendor id
        e.g. json={'user': '<user id>', 'id': '<vendor id>'}
    """
    try:
        user = request.args.get('user')
        vendorId = request.args.get('id')
        docs = vendor_ref.where("id", "==" , vendorId).get()
        if len(docs) == 1 :
            d = docs[0].to_dict()
            return jsonify({"success": True, "data" : d}), 200
        else :
            return jsonify({"success": False, "msg" : "Invalid vendor id"}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/getVendorList', methods=['GET'])
def getVendorList():
    """
        getVendorList() : Get vendor details
        Ensure you user id and vendor id
        e.g. json={'user': '<user id>'}
    """
    try:
        user = request.args.get('user')
        docs = vendor_ref.get()
        vList = []
        for doc in docs:
            vList.append(doc.to_dict())

        return jsonify({"success": True, "data" : vList}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/getService', methods=['GET'])
def getService():
    """
        getService() : Get service details
        Ensure you user id and service id
        e.g. json={'user': '<user id>', 'id': '<service id>'}
    """
    try:
        user = request.args.get('user')
        serviceId = request.args.get('id')
        docs = service_ref.where("id", "==" , serviceId).get()
        if len(docs) == 1 :
            d = docs[0].to_dict()
            return jsonify({"success": True, "data" : d}), 200
        else :
            return jsonify({"success": False, "msg" : "Invalid service id"}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/signup', methods=['POST'])
def signup():
    """
        signup() : signup user
        Ensure you pass a email and password
        e.g. json={'email': 'email@e1.com', 'password': 'e1234' , 'type' : 'employee/company_admin/vendor' }
    """
    try:
        email = request.json['email']
        docs = users_ref.where("email", "==" , email).get()
        if len(docs) > 0 :
            return jsonify({"success": False, "msg" : "Already registered email"}), 200

        js = request.get_json()
        id = {'id' : getRandomKey() }
        js.update(id)
        users_ref.add(js)
        return jsonify({"success": True, "data" : js }), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/addCompany', methods=['POST'])
def addCompany():
    """
        addCompany() : add new company to the system
        Ensure you pass  company addmin id , name , email , contact , 
        e.g. json={'user': '<company addmin id>', 'data' : {'name' : '<name>' , 'email' : '<email>' , 'contanct' : '<contact>'} }
    """
    try:
        adminId = request.json['user']
        #TODO validate admin 
        data = request.json['data']
        id = {'id' : getRandomKey() }
        admin = {'adminList' : [adminId]}
        data.update(id)
        data.update(admin)
        company_ref.add(data)
        return jsonify({"success": True, "data" : data }), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/addVendor', methods=['POST'])
def addVendor():
    """
        addVendor() : add new vendor to the system
        e.g. json={'user': '<vendor id>', 'data' : {'name' : '<name>' , 'email' : '<email>' , 'contanct' : '<contact>'} }
    """
    try:
        vendorId = request.json['user']
        #TODO validate vendor 
        data = request.json['data']
        id = {'id' : getRandomKey() }
        vendor = {'adminList' : [vendorId]}
        data.update(id)
        data.update(vendor)
        vendor_ref.add(data)
        return jsonify({"success": True, "data" : data }), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/addService', methods=['POST'])
def addService():
    """
        addService() : add new service to the system
        e.g. json={'user': '<user id>', 'data' : {'name' : '<name>' , "vendorId" : "<vendor id>" , 'email' : '<email>' , 'contanct' : '<contact>'} }
    """
    try:
        #TODO validate order
        vendor = request.json['user']
        data = request.json['data']
        vendorId = data['vendorId']
        key = getRandomKey()
        id = {'id' : key}
        data.update(id)
        service_ref.add(data)
        
        docs = vendor_ref.where("id" , "==" , vendorId).get()
        if len(docs) == 1 :
            k = docs[0].id 
            vendor_ref.document(k).update({"serviceList" : firestore.ArrayUnion([key])})
            
        return jsonify({"success": True, "data" : data }), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/addOrder', methods=['POST'])
def addOrder():
    """
        addVendor() : add new service to the system
        e.g. json={ 'user' : '<user id>' , 'companyId' : '<company id>' , 'vendorId': '<vendor id>',  'serviceId' : '<service id>' , 'status' : '<new,reject,done>' , 'timeStamp' : <timestamp>' }
    """
    try:
        #TODO validate order
        user = request.json['user']
        data = request.get_json()
        order_ref.add(data)
        return jsonify({"success": True, "data" : data }), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/addVendorToCompany', methods=['POST'])
def addVendorToCompany():
    """
        addVendorToCompany() : add new vendor to the company 
        e.g. json={'user': '<company addmin id>', 'companyId' : '<company id>' , vendorId' : '<vendor id>' }
    """
    try:
        adminId = request.json['user']
        #TODO validate admin 
        vendorId = request.json['vendorId']
        companyId = request.json['companyId']
        docs = company_ref.where("id", "==" , companyId).get()
        if len(docs) == 1 :
            k = docs[0].id 
            company_ref.document(k).update({"vendorList" : firestore.ArrayUnion([vendorId])})
            newdoc = company_ref.document(k).get()
            return jsonify({"success": True, "data" : newdoc.to_dict()}), 200
        else :
            return jsonify({"success": False, "msg" : "Invalid company id"}), 200
        #return jsonify({"success": True, "data" : data }), 200
    except Exception as e:
        return f"An Error Occured: {e}"


if __name__ == "__main__":
    app.run(debug=True)

