import socket
from typing import *


class Responses:
    HELP = "Welcome to the ATM.\n \
                     Send 'register {name} {PIN}' (space separated) to register.\n \
                     Send 'view {Name} {PIN}' to view balance.\n \
                     Send 'transact {Name} {PIN} [withdraw/deposit] {amount} to add/remove money."
    SUCCESS = "Registered Successfully!\n"
    UNAUTHORIZED = "Unauthorized.\n"
    NOT_ENOUGH = "Not enough balance\n"
    UNRECOGNIZED = "Unrecognized command\n"
    DOES_NOT_EXIST = "User does not exist\n"
    ALREADY_EXISTS = "User already exists\n"
    FULL = "The atm is full. Sorry\n"


class Account:
    def __init__(self: 'Account', PIN: str) -> None:
        self.PIN: str = PIN
        self.amount: float = 0.0

    def view(self: 'Account', PIN: str) -> str:
        if str(PIN) != self.PIN:
            return Responses.UNAUTHORIZED
        return str(self.amount)

    def transact(self: 'Account', PIN: str, change: float) -> str:
        if str(PIN) != self.PIN:
            return Responses.UNAUTHORIZED
        if self.amount + change < 0:
            return Responses.NOT_ENOUGH
        self.amount += change
        return str(self.amount)


accounts: Dict[str, Account] = {}


def handle_register(name: str, PIN: str) -> str:
    if len(accounts) == 15:
        return Responses.FULL
    if name in accounts:
        return Responses.ALREADY_EXISTS
    accounts[name] = Account(PIN)
    return Responses.SUCCESS


def handle_view(name: str, PIN: str) -> str:
    if name not in accounts:
        return Responses.DOES_NOT_EXIST
    return accounts[name].view(PIN)


def handle_transact(name: str, PIN: str, type: str, change: float) -> str:
    if name not in accounts:
        return Responses.DOES_NOT_EXIST
    if type not in ('withdraw', 'deposit'):
        return Responses.UNRECOGNIZED
    try:
        float(change)
    except ValueError:
        return Responses.UNRECOGNIZED
    return accounts[name].transact(PIN, float(change) if type == 'deposit' else -float(change))


def handle_message(msg):
    tokens = msg.split()
    if tokens[0] == 'register':
        if len(tokens) != 3:
            return Responses.UNRECOGNIZED
        return handle_register(*tokens[1:])
    elif tokens[0] == 'view':
        if len(tokens) != 3:
            return Responses.UNRECOGNIZED
        return handle_view(*tokens[1:])
    elif tokens[0] == 'transact':
        if len(tokens) != 5:
            return Responses.UNRECOGNIZED
        return handle_transact(*tokens[1:])
    elif tokens[0] == 'help':
        if len(tokens) != 1:
            return Responses.UNRECOGNIZED
        return Responses.HELP
    else:
        return Responses.UNRECOGNIZED

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 9000))
    server.listen(10)
    client, _address = server.accept()
    client.send(bytes(Responses.HELP, 'utf8'))

    while True:
        msg = client.recv(2000).decode()
        if not msg:
            server.shutdown(socket.SHUT_RDWR)
            server.close()
            break
        response = handle_message(msg.strip('\x00'))
        client.send(response.encode())

if __name__ == '__main__':
    main()