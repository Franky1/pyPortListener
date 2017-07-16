#!/usr/bin/env python
# -* coding: utf-8 *-

import logging
import socket
import os


# TCP_IP = 'localhost'
TCP_IP = '0.0.0.0'
TCP_PORT = 8080
BUFFER_SIZE = 256  # Normally 1024, but we want fast response


def get_external_ip():
    import requests
    try:
        ip = str(requests.get('http://api.ipify.org').text)
    except:
        ip = None
    logging.info('External IP address is : ' + ip)
    return ip


def listener(ip=TCP_IP, port=TCP_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(1)
    logging.info('Listening on: ' + str(sock.getsockname()))

    try:
        while True:
            conn, addr = sock.accept()
            logging.info('Connection from Address : ' + str(addr))

            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                logging.info("Received Data : " + str(data))

            conn.close()
            logging.info("Connection Closed")
    except KeyboardInterrupt:
        pass
    logging.info("Socket Closed")


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)-9s:  %(message)s', level=logging.DEBUG)
    port = os.getenv(key='PORT', default='8080')
    ip = os.getenv(key='IP', default='0.0.0.0')
    get_external_ip()
    listener(ip, port)

