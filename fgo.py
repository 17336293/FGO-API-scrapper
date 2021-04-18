#get requests package
import requests
import json
import pandas as pd

def store_data():
    url = "https://api.atlasacademy.io/export/NA/nice_servant.json"

    json_dataset = str(requests.get(url).text)

    print(len(json_dataset))  

    with open("fgo.txt", "w",  encoding='utf-8') as file:
        file.write(json_dataset)
        
#store_data()

f = open("fgo.txt","r",encoding='utf-8')
print(f)

data = json.load(f)

#df = pd.read_json(data, orient='split')

print(data[0])