import yaml
import json
import socket
import argparse
import logging
import datetime
import threading
import queue

from log import log_config

from settings import (
    HOST, PORT, BUFFERSIZE, ENCODING,
)

host = HOST
port = PORT
buffersize = BUFFERSIZE
encoding = ENCODING

parser = argparse.ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration'
)

args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        conf = yaml.load(file, Loader=yaml.Loader)
        host = conf.get('host', HOST)
        port = conf.get('port', PORT)
        buffersize = conf.get('buffersize', BUFFERSIZE)
        encoding = conf.get('encoding', ENCODING)

logger = logging.getLogger('client.main')

lock = threading.Lock()
messages = queue.Queue()


def thread_read():

    while True:
        b_data = sock.recv(buffersize)
        if b_data:
            messages.put(b_data.decode(encoding))


try:
    with socket.socket() as sock:
        sock.connect((host, port))
        logger.info('Client started')

        r_thread = threading.Thread(target=thread_read, args=(), daemon=True)
        r_thread.start()

        while True:

            while not messages.empty():
                print(messages.get())

            action = input('enter action: ')
            data = input('enter data to sent: ')

            request = json.dumps({
                'user': 'anonymous',
                'time': datetime.datetime.now().timestamp(),
                'action': action,
                'data': data
            })
            sock.send(request.encode(encoding))

except KeyboardInterrupt:
    logger.info('Client closed')
