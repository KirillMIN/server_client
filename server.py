import socket
import sys
import json
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_MASSAGE_LEN, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, MAX_DEQUE
from common.utils import get_message, send_message

"""
def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {ACCOUNT_NAME: account_name}

    }
    return out
"""


def process_client_message(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] is not None:
        return {RESPONSE: 200}
    else:
        return {RESPONSE: 400}


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.SOCK_STREAM - Создает сокет TCP,
    # socket.AF_INET - создаваемый сокет будет сетевым
    transport.bind((listen_address, listen_port))  # Присваивает порт listen_port

    # Слушаем порт

    transport.listen(MAX_DEQUE)

    while True:
        client, client_address = transport.accept()  # принятие запроса на соединение
        try:
            message_from_client = get_message(client)  # получение сообщения
            print(message_from_client)
            response = process_client_message(message_from_client)  # проверка и ответ пользователю
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()