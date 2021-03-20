from subprocess import call
from sys import argv

script, filename = argv
request_str = 'http://mipt-master.atp-fivt.org:50070/webhdfs/v1{}?op=OPEN&length=10'.format(filename)
call(["curl", "-L", request_str])
