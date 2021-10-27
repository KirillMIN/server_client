from common.variables import *
import json


def get_message(client):
    response = client.recv(MAX_MASSAGE_LEN)
    if isinstance(response, bytes):
        json_response = response.decode(ENCODING)
        response = json.loads(json_response)
        print(type(response))
        if isinstance(response, dict):
            print(response)
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    jet_message = json.dumps(message).encode()
    sock.send(jet_message)
