import sys
from classes import *

def read_splot_lines(filename):
	try:
		f = open(filename)
	except IOError:
		print 'File not found: ' + filename
		sys.exit()

	inputlines = []
	for line in f:
		parts = line.split()
		try:
			inputline = Input(float(parts[0]), float(parts[1]), float(parts[2]))
		except ValueError:
			print "Invalid input file format: " + filename
			sys.exit()

		inputlines.append(inputline)

	return inputlines