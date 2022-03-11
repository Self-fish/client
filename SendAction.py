import requests
from requests.exceptions import ConnectionError, ConnectTimeout


API_URI = "http://192.168.0.13:8082/actions"


def send_action(action, step):
    try:
        body = {"action": action, "step": step}
        resp = requests.post(API_URI, json=body)
        if resp.status_code != 200:
            print("Error connecting to the actions-api")

    except (ConnectionError, ConnectTimeout):
        print("Error connecting to the actions-api")