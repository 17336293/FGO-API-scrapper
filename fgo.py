#get requests package
import requests
import json
import pandas as pd

#access the API and store it in a test file.
def store_data():
    url = "https://api.atlasacademy.io/export/NA/nice_servant.json"

    json_dataset = str(requests.get(url).text)

    print(len(json_dataset))  

    with open("fgo.txt", "w",  encoding='utf-8') as file:
        file.write(json_dataset)

#run the store data function if no FGO file       
#store_data()

#access FGO character data
f = open("fgo.txt","r",encoding='utf-8')
print(f)

data = json.load(f)

#df = pd.read_json(data, orient='split')

print(data[0])
