# this file contains the configuration definitions

# configuration definition for continuum observations
continuumconfig="""
receiver  = 'Rcvr1_2'
beam      = 'B1'
obstype   = 'Continuum'
backend   = 'DCR'
nwin      = 1
restfreq  = 1400
bandwidth = 80
swmode    = 'tp'
swtype    = 'none'
swper     = 0.2
tint      = 0.2
vframe    = 'topo'
vdef      = 'Radio'
noisecal  =  'lo'
pol       = 'Linear'
"""
# configuration definition for spectral line observations
# using frequency switching
vegas_fs_config="""
receiver = 'Rcvr1_2'  
beam = 'B1' 
obstype = 'Spectroscopy'
backend = 'VEGAS'
nwin = 1
restfreq = 1420 
bandwidth = 23.44 
swmode = 'sp' 
swtype = 'fsw'
swper = 1.0
swfreq = 0, -2.5
tint = 2.0 
vframe = 'lsrk'
vdef = 'Radio'
nchan = 'medium-high'
vegas.subband = 1
noisecal = 'lo'
pol = 'Linear'
"""

# configuration definition for multiple spectral line observations
# using position switching
vegas_ps_config="""
receiver  = 'Rcvr8_10'
obstype   = 'Spectroscopy'
backend   = 'VEGAS'
nwin      = 9
restfreq  = 9816.867, 9487.824, 9173.323, 8872.571, 
            9820.9, 9821.5, 9822.6, 9823.4, 9824.6
deltafreq = 0
dopplertrackfreq = 8873.1
bandwidth = 23.44 
swmode    = 'tp'
swtype    = 'none'
swper     = 1.0
tint      = 30 
vlow      = 0
vhigh     = 0
vframe    = 'lsrk'
vdef      = 'Radio'
noisecal  = 'lo'
pol       = 'Circular'
nchan     = 'medium-low'
"""

# configuration definition for spectral line observations
# using a multi-beam receiver for nodding observations
vegas_nod_config="""
receiver  = 'RcvrArray18_26'
beam      = '1,2'
obstype   = 'Spectroscopy'
backend   = 'VEGAS'
nwin      = 4
restfreq  = 23694.495, 23722.633, 23870.129, 25056.025
deltafreq = 0,0,0,0
bandwidth = 100  
swmode    = 'tp'
swtype    = 'none'
swper     = 1.0
tint      = 30 
vlow      = 0
vhigh     = 0
vframe    = 'lsrk'
vdef      = 'Radio'
noisecal  =  'lo'
pol       = 'Circular'
nchan     =  'low'
"""

#configuration for VEGAS and KFPA
vegas_kfpa_config="""
receiver  = 'RcvrArray18_26'
beam      = 'all'
obstype   = 'Spectroscopy'
backend   = 'VEGAS'
restfreq  = {24000:"1,2,3,4", 23400:"5,6,7", 25500 : '-1', 
             "DopplerTrackFreq": 25500} 
deltafreq = {24000:0, 23400:0, 25500:0} 
bandwidth = 187.5  
swmode    = 'tp'
swtype    = 'none'
swper     = 1.0
tint      = 30 
vlow      = 0
vhigh     = 0
vframe    = 'lsrk'
vdef      = 'Radio'
noisecal  = 'lo'
pol       = 'Circular'
nchan     = 'low'
vegas.vpol= 'cross'
"""

# configuration definition for spectral line observations
# with KFPA 
vegas_kfpa_aconfig="""
receiver  = 'RcvrArray18_26'
obstype   = 'Spectroscopy'
backend   = 'VEGAS'
swmode    = 'tp'
swtype    = 'none'
swper     = 1.0
tint      = 30 
vlow      = 0
vhigh     = 0
vframe    = 'lsrk'
vdef      = 'Radio'
noisecal  =  'lo'
pol       = 'Circular'
dopplertrackfreq = 25500
bandwidth = 187.5  
nchan     =  'low'
deltafreq = 0
vegas.vpol='cross'
restfreq=[{"restfreq":24000, "beam":"1,2,3,4"},
          {"restfreq":25000, "beam":"1"},
          {"restfreq":23400, "beam":"5,6,7"}]
"""

# configuration definition for multiple spectral line observations
# using frequency switching
vegas_fs_aconfig="""
receiver = 'Rcvr1_2'
beam     = 'B1'
obstype  = 'Spectroscopy'
backend  = 'VEGAS'
swmode   = 'sp'
swtype   = 'fsw'
swper    = 1.0
swfreq   = 0, 5
tint     = 10.0
vlow     = 0
vhigh    = 0
vframe   = 'lsrk'
vdef     = 'Radio'
noisecal = 'lo'
pol      = 'Linear'
dopplertrackfreq=1420.405
bandwidth=15.625
restfreq = [ {"restfreq":1420.405, "bandwidth":15.625, "res":0.24, 
                                      "deltafreq":0, "vpol":"cross"},
                {"restfreq":1612.231, "bandwidth":15.625, "res":1.9, 
                                                      "deltafreq":0}, 
                {"restfreq":1665.402, "bandwidth":15.625, "res":0.24, 
                                      "deltafreq":1, "vpol":"cross"}, 
                {"restfreq":1667.359, "bandwidth":15.625, "res":0.24, 
                                      "deltafreq":0, "vpol":"cross"}, 
                {"restfreq":1720.530, "bandwidth":15.625, "res":1.9, 
                                                       "deltafreq":0},
                {"restfreq":1350.414, "bandwidth":23.44, "res":0.7, 
                                             "deltafreq":0, "tint":1.0},
                {"restfreq":1532.557, "bandwidth":100, "res":1.5, 
                                                      "deltafreq":0}]
"""


