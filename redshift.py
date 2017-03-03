print('Please specify all wavelengths in Angstroms, A. (100nm = 1000A)')
L_emit=input('Enter the wavelength of the light emitted at the source:')
L_measure=input('Enter the wavelength of the light measured in the lab:')

L_emit=float(L_emit)
L_measure=float(L_measure)

z=(L_measure/L_emit)-1

print('The redshift of the observed object is:', round(z,3))
