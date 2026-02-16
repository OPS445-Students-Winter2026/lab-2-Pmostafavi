#!/usr/bin/env python3

# Author: Pouya Mostafavi
# AuthorID: pmostafavi
# Date Created: 2026/02/16

import sys

if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) == 2:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
if timer == 0:
    print('blast off!')