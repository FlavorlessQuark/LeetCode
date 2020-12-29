import sys
import os
import re

files = os.listdir()
filenames = []
maximum = 0

for x in files:
	num = re.findall(r'(\d+)', x)
	if num:
		maximum = max(int(num[0]), maximum)
		filenames.append((x, num[0]))

l = len(str(maximum))

for x in filenames:
	s = x[0].replace(x[1], x[1].rjust(l, '0'))
	os.rename(x[0], s)
