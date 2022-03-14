import requests
import json
from requests.exceptions import ConnectionError, ConnectTimeout
from requests.structures import CaseInsensitiveDict


ACTION_API_URI = "http://192.168.0.13:8082/actions"
UPDATE_API_URI = "http://192.168.0.13:8081/preferences"


def send_action(action, step):
    try:
        body = {"action": action, "step": step}
        resp = requests.post(ACTION_API_URI, json=body)
        if resp.status_code != 200:
            print("Error connecting to the actions-api")

    except (ConnectionError, ConnectTimeout):
        print("Error connecting to the actions-api")


def update_light_preferences():
    try:
        body = {'lightsPreferences': {'mode': 'AUTOMATIC', 'range': {'starting': '14:00', 'finishing': '23:59'}}, 'deviceId': 'sf-000000009df9b724'}
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        json_object = json.dumps(body)
        result = requests.put(UPDATE_API_URI, headers=headers, data=json_object)
        if result.status_code != 200:
            print("Error connecting to the preferences-api")
    except (ConnectionError, ConnectTimeout):
        print("Error connecting to the preferences-api")
