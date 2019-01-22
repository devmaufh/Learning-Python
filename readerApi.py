import json
import requests 
import pandas as pd
url="https://jsonplaceholder.typicode.com/todos"
def get_json(url):
    response=requests.get(url)
    return response.json()

def generate_file(url):
    data=pd.read_json(url)
    data.to_json("file.json")
   
generate_file(url)
for i in get_json(url):
    print ("A ver: ",i["userId"],i["title"])