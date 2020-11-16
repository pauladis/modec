import requests
import json
import jsonpath


def test_create_new_equipment_by_query_params():
    url = "http://127.0.0.1:8000/equipment/?vessel=MV102"
    body = {
    "name":"container-141",
    "code":"C141",
    "location":"brazil"
    }
    response = requests.post(url, body)
    assert response.status_code == 201


def test_create_new_equipment_by_body_params():
    url = "http://127.0.0.1:8000/equipment/"
    body = {
    "name":"container-150",
    "code":"C150",
    "location":"brazil",
    "vessel":"MV102"
    }
    response = requests.post(url, body)

    assert response.status_code == 201

def test_deactivate_single_equipment():
    url = "http://127.0.0.1:8000/equipment/deactivateEquipment/"
    body = {"code":["C139"]}
    response = requests.patch(url, body)

    assert response.status_code == 200

def test_deactivate_list_equipment():
    url = "http://127.0.0.1:8000/equipment/deactivateEquipment/"
    body = {"code":["C139","C150"]}
    response = requests.patch(url, body)

    assert response.status_code == 200

def test_activate_single_equipment():
    url = "http://127.0.0.1:8000/equipment/activateEquipment/"
    body = {"code":["C139"]}
    response = requests.patch(url, body)

    assert response.status_code == 200

def test_activate_list_equipment():
    url = "http://127.0.0.1:8000/equipment/activateEquipment/"
    body = {"code":["C139","C150"]}
    response = requests.patch(url, body)

    assert response.status_code == 200


def test_create_new_equipment_with_duplicate_code():
    url = "http://127.0.0.1:8000/equipment/?vessel=MV102"
    body = {
    "name":"container-141",
    "code":"C141",
    "location":"brazil"
    }
    response = requests.post(url, body)
    assert response.status_code == 400