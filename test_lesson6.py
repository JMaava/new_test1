import pytest
import requests

base_url = 'https://restful-booker.herokuapp.com/booking'
auth_url = 'https://restful-booker.herokuapp.com/auth'

# pytest -k 'поиск по слову'
# pytest -v расширенный отчет
@pytest.fixture(scope='module')
# scope='module' - применится ко всем тестам, запускается 1 раз
def auth_token():
    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    responce = requests.post(auth_url, json=auth_data)
    token = responce.json()["token"]
    yield token

@pytest.fixture(scope="session")
def booking_id():
    payload = {
        "firstname": "Joe",
        "lastname": "Bread",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-02-01"
        },
        "additionalneeds": "Breakfast"
    }

    responce = requests.post(base_url, json=payload)
    bookingid = responce.json()['bookingid']
    yield bookingid

# возможность выполнить что-то после возврата в ф-ции

# def summ(x,y):
#     return x + y
#
# def test_equal():
#     assert summ(5,8) == 13

def create_booking(name, surname):
    data = {
    "firstname": name,
    "lastname": surname,
    "totalprice": 150,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "2024-01-01",
        "checkout": "2024-02-01"
    }
    }
    token = {"Cookie": f"token={auth_token}"}
    responce = requests.post(base_url, headers=token, json = data)
    return responce.json()

@pytest.mark.xfail(reason = 'wrong status code')
# тест должен упасть - если пройдет, будет пометка XPASS
# @pytest.mark.skip
def test_get_code():
    result = requests.get(base_url)
    assert result.status_code == 400

# @pytest.mark.smoke
def test_booking_by_id(booking_id):
    print(booking_id)
    responce = requests.get(f'{base_url}/{booking_id}')
    responce_data = responce.json()
    expected_keys = [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
    ]
    assert responce.status_code == 200
    assert len(responce_data.keys()) == len(expected_keys)
    for key in expected_keys:
        assert key in responce_data.keys()

# def test_create_book(booking_id):
#     responce = requests.post(base_url, json=payload)
#     print(responce.json()['bookingid'])
#     assert responce.status_code == 200

def test_creating_check(booking_id):
    result = requests.get(f"{base_url}/{booking_id}")
    print(result.json())
    assert result.status_code == 200
    assert result.json()['firstname'] == 'Joe'


def test_update(auth_token, booking_id):
    payload = {
        "firstname": "Joe",
        "lastname": "Bread",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-02-01"
        },
        "additionalneeds": "Lunch"
    }
    token = {"Cookie": f"token={auth_token}"}

    responce = requests.put(f'{base_url}/{booking_id}', json = payload, headers=token)
    assert responce.status_code == 200
    responce2 = requests.get(f'{base_url}/{booking_id}')
    print(responce2.json())
    assert responce2.json()["additionalneeds"] == "Lunch"

# def test_delete_booking(booking_id, auth_token):
#     token = {"Cookie": f"token={auth_token}"}
#     response = requests.delete(f'{base_url}/{booking_id}', headers=token)
#     assert response.status_code == 201
#     response_get = requests.get(f'{base_url}/{booking_id}')
#     assert response_get.status_code ==404

def test_create_and_patch(auth_token, booking_id):
    # name = 'Theodor'
    # surname = 'Smith'
    new_name = 'Theo'
    new_surname = 'Patterson'

    # booking = create_booking(name=name, surname=surname)

    url = f'{base_url}/{booking_id}'
    new_data = {
        "firstname": new_name,
        "lastname": new_surname
    }

    token = {'Cookie': f'token={auth_token}'}
    response = requests.patch(url, headers=token, json=new_data)
    response2 = requests.get(url)
    result = response2.json()
    print(result)

    assert response.status_code == 200
    assert response2.status_code == 200
    assert result['firstname'] == new_name
    assert result['lastname'] == new_surname

#     # response = requests.patch(url=url, headers=token, json=new_data)
#     #
#     # print(response.json())