import requests
import json
import jsonpath


def test_create_new_vessel():
    url = "http://127.0.0.1:8000/vessel/"
    body = {"code": "MV102"}
    response = requests.post(url, body)

    assert response.status_code == 201


def test_get_vessels():
    url = "http://127.0.0.1:8000/vessel/"
    response = requests.get(url)

    assert response.status_code == 200


def test_get_valid_equipment_by_vessel_status_code():
    url = "http://127.0.0.1:8000/vessel/MV102/equipment"
    response = requests.get(url)

    assert response.status_code == 200


def test_create_new_vessel_with_duplicate_code():
    url = "http://127.0.0.1:8000/vessel/"
    body = {"code": "MV102"}
    response = requests.post(url, body)

    assert response.status_code == 400