#!/usr/bin/env python
# -* coding: utf-8 *-

import logging
import socket
import os


# TCP_IP = 'localhost'
IP = '0.0.0.0'
PORT = 5055
BUFFER_SIZE = 256  # Normally 1024, but we want fast response


def get_external_ip():
    import requests
    try:
        ip = str(requests.get('http://api.ipify.org').text)
    except:
        ip = None
    logging.info('External IP address is : ' + ip)
    return ip


def listener(ip=IP, port=PORT, proto=socket.SOCK_STREAM):
    sock = socket.socket(socket.AF_INET, proto)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, port))
    if proto == socket.SOCK_STREAM:
        sock.listen(1)
    logging.info('Listening on: ' + str(sock.getsockname()))

    try:
        while True:
            if proto == socket.SOCK_STREAM:
                conn, addr = sock.accept()
                logging.info('Connection from Address : ' + str(addr))

            while True:
                if proto == socket.SOCK_STREAM:
                    data = conn.recv(BUFFER_SIZE)
                    if not data:
                        break
                    logging.info("Received Data : " + str(data))
                elif proto == socket.SOCK_DGRAM:
                    data, addr = sock.recvfrom(BUFFER_SIZE)
                    if not data:
                        break
                    logging.info("Received From : " + str(addr) + " Data : " + str(data))

            conn.close()
            logging.info("Connection Closed")
    except KeyboardInterrupt:
        pass
    logging.info("Socket Closed")


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)-9s:  %(message)s', level=logging.DEBUG)
    port = os.getenv(key='PORT', default='5055')
    ip = os.getenv(key='IP', default='0.0.0.0')
    get_external_ip()
    listener(ip=IP, port=PORT, proto=socket.SOCK_STREAM)
