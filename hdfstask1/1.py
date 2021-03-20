from sys import argv
from subprocess import check_output
import re

script, filename = argv

out_str = check_output(["hdfs", "fsck", filename, "-files", "-blocks", "-locations"])

res = re.search(rb'blk_\d+_', out_str)

main_str = check_output(["hdfs", "fsck", "-blockId", out_str[res.start():res.end()-1]])

main_res = re.search(rb'mipt-node\S+.org', main_str)
print(main_str[main_res.start():main_res.end()].decode('utf-8'))
