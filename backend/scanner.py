import socket


target = "192.168.1.11"


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True

    except:
        return False


for port in range(1, 1024):
    result = portscan(port)
    if (result):
        print('Port {} is open'.format(port))
    else:
        print('Port {} is closed.'.format(port))
