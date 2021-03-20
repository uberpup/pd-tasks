from sys import argv
from subprocess import call, check_output
import re

script, size = argv

call(["dd", "if=/dev/zero", "of=output_.dat", "bs={}".format(size), "count=1"])
call(["hdfs", "dfs", "-put", "-l", "output_.dat", "/tmp/output_.dat"])

out_str = check_output(["hdfs", "fsck", "/tmp/output_.dat", "-files", "-blocks", "-locations"])
res = re.findall(rb'blk_\d+', out_str)

exp_size = 0

for blockId in res:
	main_str = check_output(["hdfs", "fsck", "-blockId", blockId])
	main_res = re.search(rb'mipt-node\S+.org', main_str)
	server_name = main_str[main_res.start():main_res.end()].decode('utf-8')
	out_str = check_output(["sudo", "-u", "hdfsuser", "ssh", "hdfsuser@{}".format(server_name), "find", "/dfs", "-name", blockId])
	block_size = check_output(["sudo", "-u", "hdfsuser", "ssh", "hdfsuser@{}".format(server_name), "stat", "--format=%s", out_str[0:len(out_str)-1].decode('utf-8')])
	exp_size += int(block_size)

print((str(int(size) - exp_size)), end="")

call(["hdfs", "dfs", "-rm", "/tmp/output_.dat"])
call(["rm", "output_.dat"])
