from common.files import *

def run(args):
	red = args.filename[0]
	redlines = read_splot_lines(red)
	
	for line in redlines:
		line.identify()
		if line.identified_line is not None:
			print line.identified_line.wavelength
		else:
			print 'None'
