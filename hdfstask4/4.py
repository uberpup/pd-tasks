from sys import argv
from subprocess import call, check_output
import re

script, blockId = argv

main_str = check_output(["hdfs", "fsck", "-blockId", blockId])

main_res = re.search(rb'mipt-node\S+.org', main_str)
server_name = main_str[main_res.start():main_res.end()].decode('utf-8')

out_str = check_output(["sudo", "-u", "hdfsuser", "ssh", "hdfsuser@{}".format(server_name), "find", "/dfs", "-name", blockId])

print(server_name, ':', out_str.decode('utf-8'), sep="", end="")
