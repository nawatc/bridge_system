import re


txt = "N:QJT5432.T.6.QJ82 E:.J97543.K7532.94 S:87.A62.QJT4.AT75 W:AK96.KQ8.A98.K63"
x = re.match("N:([AKQJT98765432]+)\.\S\.", txt)

print(x.group())
