import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'

def test_create_pet():
    url = f'{base_url}/pet'
    data = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "Vasiliy"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "myPet"
        }
      ],
      "status": "available"
    }

    response = requests.post(url, data=data)

    print (response.json())