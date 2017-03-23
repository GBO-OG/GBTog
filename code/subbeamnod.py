#Example 1 - nodLength units in seconds (default)
SubBeamNod('3C48', scanDuration=60.0, beamName='MR12',
           nodLength=4.4826624)

#Example 2 - nodLength units are "tint" as set in the configuration
SubBeamNod('3C48', scanDuration=60.0, beamName='MR12', 
           nodLength=3, nodUnit='integrations')
