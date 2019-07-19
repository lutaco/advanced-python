import socket
import yaml
import argparse
import logging
import select
from log import log_config

from handlers import default_handler
from settings import HOST, PORT, BUFFERSIZE, ENCODING


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

logger = logging.getLogger('server.main')

clients = []
requests = []

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    sock.settimeout(0)
    logger.info('server started')

    while True:

        try:
            client, address = sock.accept()
            logger.info(f'client with address {address}, fd {client.fileno()} was detected')
            clients.append(client)
        except OSError as e:
            pass

        r = []
        w = []

        try:
            r, w, e = select.select(clients, clients, [], 0)
        except Exception as e:
            pass

        for r_client in r:
            try:
                b_request = r_client.recv(buffersize)

                if not b_request:
                    raise socket.error

                requests.append(b_request)
            except:
                logger.info(f'client (fd={r_client.fileno()}) disconnected')
                clients.remove(r_client)

        if len(requests) != 0:
            b_request = requests.pop()
            response = default_handler(b_request.decode(encoding))
            b_response = response.encode(encoding)

            for w_client in w:
                try:
                    w_client.send(b_response)
                except:
                    logger.info(f'client {w_client.fileno()} disconnected')
                    clients.remove(w_client)


except KeyboardInterrupt:
    logger.info('server closed')
