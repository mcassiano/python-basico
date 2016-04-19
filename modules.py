#!/usr/bin/python
import sys
import math

from fractions import Fraction
from decimal import Decimal

args = sys.argv[1:]

for arg in args:
	print(arg)

degrees = list(range(0, 91))

x = list(map(math.radians, degrees))
y = list(map(math.sin, x))

interesting = [0, 30, 90]

for i in interesting:
	print(degrees[i], Fraction(Decimal(y[i])).limit_denominator())