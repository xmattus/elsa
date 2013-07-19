# This is the ELSA config file. Variables below define how ELSA operates. Some of them can be overridden on the command line. See the documentation for more details.

# The former "wavelengths file" config variable is now wavelengths.py.

# Search box bounds to identify wavelengths in the optical (angstroms). For example: for a value of 4.0, ELSA will identify wavelengths within 6564 A +/- 4.0 A as Halpha.
max_tolerance_optical = 4.0

# Same, for IR lines.
max_tolerance_infrared = 750.0

# Reference wavelengths of the hydrogen Balmer series and Helium pickering series (for extinction calculations)
# Note these are not the same as their counterparts in wavelengths.py, though you will most likely want them the same.
lam_halpha = 6563.0
lam_hbeta = 4681.0
lam_hgamma = 4340.0
lam_hdelta = 4101.0
lam_hepsilon = 3968.0
lam_he2 = 4686.0

# Set to true if you want to skip ELSA's extinction correction when computing abundances.
skip_dereddening = False

# Set to true if you want to skip ELSA's iterative computation of the Balmer line ratios used in extinction correction.
skip_balmer_convergence = False

# Reference ratios of the ratios of Balmer lines typical of nebular environments. Used if skip_balmer_convergence is true.
ratio_halpha_hbeta = 2.86
ratio_hgamma_hbeta = 0.469

# Set to true if you want to skip ELSA's deblending of the helium Pickering lines that overlay the Balmer lines.
skip_line_deblending = False