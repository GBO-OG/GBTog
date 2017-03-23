# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# 4mm line setup FL2 77GHz
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

wband_config = '''
receiver  = 'Rcvr68_92'
beam      = '1,2'
obstype   = 'Spectroscopy'
backend   = 'VEGAS'
restfreq  = 77000.,77000.
bandwidth = 1500
swmode    = 'tp_nocal'
swtype    = 'none'
swper     = 0.2
tint      = 1.0
vframe    = 'lsrk'
vdef      = 'Radio'
pol       = 'Linear'
nchan     = 'low'
iftarget  = 1.5
'''

