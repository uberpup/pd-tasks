#!/usr/bin/env python3

import sys
import random

step = 0
current_key = ''
printed_overall = 0

for line in sys.stdin:
    try:
        mod_id = line[1:].strip()
    except ValueError as e:
        continue
		#if (printed_overall == 50 and current_key == 1) or (printed_overall == 49 and current_key == 0):
		#	break
    if step == 0:
        if current_key != '':
            print(current_key)
            current_key = ''
            printed_overall += 1
        step = random.randint(1, 5)

    if current_key == '':
        current_key = mod_id
    else:
        current_key += ',' + mod_id
    step -= 1

if current_key:
    print(current_key)
    printed_overall += 1
