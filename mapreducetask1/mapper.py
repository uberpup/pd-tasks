#!/usr/bin/env python3

import sys
import random

for line in sys.stdin:
	id = str(random.randint(1, 5)) + line.strip()
	print(id)
