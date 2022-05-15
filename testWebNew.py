from cgi import test
from flask import json
from flask import Flask, request, jsonify
import requests

#api_url = 'https://db-service-w5p4snpova-uc.a.run.app' 
api_url = "https://db-service-jbibgdeidq-uc.a.run.app"
#api_url = 'http://127.0.0.1:5000'

def test_login_pass():  
    din =   { 'username' : 'employee111@mail.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)
    #response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 500

def test_login_fail():  
    din =   { 'username' : 'employee111@mail.com', 'password' : 'e1111'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)
    #response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 500

def test_get_vendors():  
    din =   { 'username' : 'employee111@mail.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(data["token"])
    token = data["token"]

    din =   { 'token' : token}   
    url = api_url + "/getVendorList"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_get_vendors_all():  
    din =   { 'username' : 'employee111@mail.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(data["token"])
    token = data["token"]

    din =   { 'token' : token}   
    url = api_url + "/getVendorListAll"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_add_vendor():  
    din =   { 'username' : 'employee111@mail.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(data["token"])
    token = data["token"]

    din =   { 'token' : token , 'vendor' : "vendor222"}   
    url = api_url + "/addNewVendor"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_remove_vendor():  
    din =   { 'username' : 'employee111@mail.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(data["token"])
    token = data["token"]

    din =   { 'token' : token , 'vendor' : "vendor111"}   
    url = api_url + "/removeVendor"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_signup_employee():
    din =   { 'username' : 'employee333@mail.com', 'password' : 'e1234' , 'type' : 'employee' , "company" : "company222"}   
    url = api_url + "/signup"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_signup_vendor():
    din =   { 'username' : 'vendor333@mail.com', 'password' : 'v1234' , 'type' : 'vendor' , "company" : "vendor333"}   
    url = api_url + "/signup"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_add_order1():
    din =   { 'username' : 'employee111@mail.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(data["token"])
    token = data["token"]

    din =   { 'token' : token , 'customerName' : "customer111" , 'email' : "customer111@mail.com" , 'contact': "11112233" ,  'vendor' : "vendor111" , 'details' :  "1 pizza"}  
    url = api_url + "/addOrder"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_add_order2():
    din =   { 'username' : 'employee222@mail.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(data["token"])
    token = data["token"]

    din =   { 'token' : token , 'customerName' : "customer222" , 'email' : "customer222@mail.com" , 'contact': "43544787978" ,  'vendor' : "vendor222" , 'details' :  "1 soup"}  
    url = api_url + "/addOrder"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_orders_history_vendor():
    din =   { 'username' : 'vendor111@mail.com', 'password' : 'v1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(response.json())
    token = data["token"]

    din =   { 'token' : token }  
    url = api_url + "/getOrderHistory"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_orders_history_employee():
    din =   { 'username' : 'employee111@mail.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(response.json())
    print(data["token"])
    token = data["token"]

    din =   { 'token' : token }  
    url = api_url + "/getOrderHistory"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_orders_history_admin():
    din =   { 'username' : 'admin111@mail.com', 'password' : 'ca1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(response.json())
    print(data["token"])
    token = data["token"]

    din =   { 'token' : token }  
    url = api_url + "/getOrderHistory"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())

    assert response.status_code == 500

def test_change_orders_vendor():
    din =   { 'username' : 'vendor111@mail.com', 'password' : 'v1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(response.json())
    token = data["token"]

    din =   { 'token' : token }  
    url = api_url + "/getOrderHistory"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())
    data = response.json()
    orderlist = data["orderList"]
    order0 = orderlist[0]
    orderid = order0["id"]

    print(orderid)

    din =   { 'token' : token, "orderId" : orderid , "status" : "accepted" }  
    url = api_url + "/changeOrderStatus"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)
    print(response.json())

    assert response.status_code == 500

def test_get_orders_by_status():
    din =   { 'username' : 'vendor222@mail.com', 'password' : 'v1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(response.json())
    token = data["token"]

    din =   { 'token' : token , 'status' : 'new'}  
    url = api_url + "/getOrdersByStatus"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())
    assert response.status_code == 500


def test_get_orders_stat():
    din =   { 'username' : 'vendor222@mail.com', 'password' : 'v1234'}   
    url = api_url + "/login"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    data = response.json() 
    print(response.json())
    token = data["token"]

    din =   { 'token' : token }  
    url = api_url + "/getOrdersStat"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)

    print(response.json())
    assert response.status_code == 500
