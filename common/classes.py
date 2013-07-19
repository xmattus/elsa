from constants import *
from config import *
from wavelengths import *

class Line:
	def __init__(self, atom, stage, wavelength, forbidden):
		self.atom = atom
		self.stage = stage
		self.wavelength = wavelength
		self.energy = (h*c) / wavelength
		self.forbidden = forbidden

class Input:
	def __init__(self, wavelength, continuum, flux):
		self.wavelength = wavelength
		self.continuum = continuum
		self.flux = flux

	def identify(self):
		self.identified_line = None
		for line in config_emission_lines:
			print "%f %f %f\n" % (self.wavelength, line.wavelength - max_tolerance_optical, line.wavelength + max_tolerance_optical)
			if self.wavelength > (line.wavelength - max_tolerance_optical) and self.wavelength < (line.wavelength + max_tolerance_optical):
				self.identified_line = line	
