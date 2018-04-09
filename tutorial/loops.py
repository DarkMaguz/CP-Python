#!/usr/bin/python

import sys

# Der findes flere slags loekker i python, men kun 2 af dem skal vi arbejde med i dag.

# for leokken:
for x in range(1,10):
	print("x er nu " + str(x))

try:
    input("Tryk ctrl+c for at afbryde.\nTryk paa en vilkaarlig tast for at forsaette.")
except SyntaxError:
    pass

i=0
# While loekke:
while True:
	print("Jeg kan en sang der kan drive dig til vandvid!\t" + str(i) )
	i += 1
