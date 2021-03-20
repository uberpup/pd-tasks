#!/usr/bin/env python3

import sys

sum = 0
cur_key = 0
for line in sys.stdin:
	try:
		key, count = line.strip().split('\t', 1)
		count = int(count)
	except ValueError as e:
		continue
	if cur_key != key:
		if cur_key:
			print(cur_key, '\t', sum, sep="")
		sum = 0
		cur_key = key
	sum += count

if cur_key:
	print(cur_key, '\t', sum, sep="")
