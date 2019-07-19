import requests
import pprint

try:
    r = requests.get('https://api.github.com/events')
    #print r.headers['Content-Type']
except requests.exceptions.HTTPError as e:
    print "some thing failed: ",e.response.status_code
 
task = {"summary": "Take out trash", "description": "" }
resp = requests.post('https://todolist.example.com/tasks/', json=task)
if resp.status_code != 201:
    print "Error occured with status code: ",resp.status_code
