import yaml
import argparse

from settings import ENCODING

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
        encoding = conf.get('encoding', ENCODING)

try:
    print('Client started')
    value = input('enter data to sent: ')
    bvalue = value.encode(encoding)
    bvalue.decode()
except KeyboardInterrupt:
    print('Client closed')
