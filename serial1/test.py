import requests
import json
import time
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
print('get request')
def get_resources(id=None):
    data={}
    if id is not None:
        data={
        'id':id
        }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resources()
time.sleep(5)

'''import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'''
print("post request")
def create_resources():
    new_emp={
        'eno':601,
        'ename':'shiva ff teddy',
        'esal':40000,
        'eaddr':'ranchiooo'
        }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
create_resources()
time.sleep(10)
print("update request")
def update_resource(id):
    new_data={
    'id':id,
    'esal':999999,
    #'eaddr':'chennai',
    #'ename':'ritesh',
    #'eno':10
    }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())
update_resource(3)
time.sleep(10)
print('delete')
def delete_resource(id):
    new_data={
    'id':id,
    #'esal':999999,
    #'eaddr':'chennai',
    #'ename':'ritesh',
    #'eno':10
    }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())
delete_resource(3)
