#!/usr/bin/env python3

import sys
import re

met_already = set()
for line in sys.stdin:
	try:
		art_id, txt = line.strip().split('\t', 1)
	except ValueError as e:
		continue
	words = re.split('[^A-Za-z]+', txt.strip(), flags=re.UNICODE)
	for i in range(0, len(words) - 1):
		res = words[i].lower() + ' ' + words[i + 1].lower()
		if res in met_already:
			continue
		else:
			print(res, '\t', 1, sep="")
		met_already.add(res)
	met_already.clear()
