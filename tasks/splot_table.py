from common.files import *

def run(args):
	red = args.filename[0]
	redlines = read_splot_lines(red)
	
	for line in redlines:
		if hasattr(args, 'redshift'):
			line.apply_redshift(float(args.redshift))
		line.identify()
		if line.identified_line is not None:
			print line.obs_wavelength
			print line.identified_line.wavelength
		
