#from app import app
from cgi import test
from flask import json
from flask import Flask, request, jsonify
import requests

api_url = 'https://db-service-w5p4snpova-uc.a.run.app' 
#api_url = 'http://127.0.0.1:5000'

def test_login_pass():  
    din =   { 'email' : 'email@e1.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_login_invalid_password():  
    din =   { 'email' : 'email@e1.com', 'password' : 'e1234_invalid'}   
    url = api_url + "/login"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_login_invalid_email():  
    din =   { 'email' : 'invalid_email@e1.com', 'password' : 'e1234'}   
    url = api_url + "/login"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400


def test_getcompany():  
    din =   { 'user' : 'ca1111', 'id' : 'c1111'}   
    url = api_url + "/getCompany"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_getcompany_invalid():  
    din =   { 'user' : 'ca2222', 'id' : 'c1111_invalid'}   
    url = api_url + "/getCompany"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_getvendor():  
    din =   { 'user' : 'va1111', 'id' : 'v1111'}   
    url = api_url + "/getVendor"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_getvendorlist():  
    din =   { 'user' : 'ca1111'}   
    url = api_url + "/getVendorList"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_getvendor_invalid():  
    din =   { 'user' : 'va2222', 'id' : 'viiii'}   
    url = api_url + "/getVendor"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_getservice():  
    din =   { 'user' : 'va1111', 'id' : 's1111'}   
    url = api_url + "/getService"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_getservice_invalid():  
    din =   { 'user' : 'va2222', 'id' : 'siiii'}   
    url = api_url + "/getService"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_signup():  
    din =   {"email" : "email@e101.com", "password":"e3456", "type" : "employee" }   
    url = api_url + "/signup"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)
    
    print(response.json())
    assert response.status_code == 400


def test_addcompany():  
    din =  {'user': 'ca5555', 'data' : {'name' : 'zero' , 'email' : 'email@zero.com' , 'contanct' : '077556622'} }  
    url = api_url + "/addCompany"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)
    
    print(response.json())
    assert response.status_code == 400

def test_addvendor():  
    din =  {'user': 'v5555', 'data' : {'name' : 'hot pot' , 'email' : 'email@hotpot.com' , 'contanct' : '077556622'} }  
    url = api_url + "/addVendor"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)
    
    print(response.json())
    assert response.status_code == 400

def test_addorder():  
    din =  {'user' : 'e1111' , 'companyId' : 'c1111' , 'vendorId': 'v1111',  'serviceId' : 's1111' , 'status' : 'new' , 'timeStamp' : '2022-04-01 20:20'}  
    url = api_url + "/addOrder"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)
    
    print(response.json())
    assert response.status_code == 400

def test_getCompanyForAdmin():
    din =   { 'user' : 'ca1111'}   
    url = api_url + "/getCompanyForAdmin"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_getCompanyForEmployee():
    din =   { 'user' : 'e1111'}   
    url = api_url + "/getCompanyForEmployee"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_getVendorForAdmin():
    din =   { 'user' : 'va1111'}   
    url = api_url + "/getVendorForAdmin"
    response = requests.get(url , params=din)
    
    #data = json.loads(response.get_data(as_text=True))
    print(response.json())
    assert response.status_code == 400

def test_addVendorToCompany():  
    din =  {'user': 'ca1111', 'companyId': 'c1111' , 'vendorId' : 'v6699' }  
    url = api_url + "/addVendorToCompany"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)
    
    print(response.json())
    assert response.status_code == 400

def test_addservice():  
    din =  {'user': 'va1111', 'data' : {"vendorId" : "v1111" , 'name' : 'yello-rice' , 'description' : 'yellow rice' , 'price' : '560'} }  
    url = api_url + "/addService"
    headers =  {"Content-Type":"application/json"}
    response = requests.post(url , data=json.dumps(din) , headers=headers)
    
    print(response.json())
    assert response.status_code == 400


