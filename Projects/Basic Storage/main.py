import requests
import json

pantryID = os.environ['SEC_TOKEN']

pantry = (f'https://getpantry.cloud/apiv1/pantry/{pantryID}/basket/testBasket')

def requestData():
    data = requests.get(pantry).json()
    data = json.dumps(data, indent=2)
    return data


Person = json.dumps({
  "name": "Jomma",
  "Is Awesome": True,
  "Age": 22
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", pantry, headers=headers, data=Person)

print(requestData())
