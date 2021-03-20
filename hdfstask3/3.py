from hdfs import Config
from sys import argv
from math import ceil

script, filename = argv

client = Config().get_client()

status = client.status(filename)

print(ceil(status['length'] / status['blockSize']))


