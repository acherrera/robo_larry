#!/usr/bin/python3

# import sys
# 
# for line in sys.stdin:
#     sys.stdout.write(line)

import os
with os.popen('sudo showkey') as pse:
    for line in pse:
        print(line)
