#Configure for correct receiver at start of session...
execfile('/home/astro-util/projects/GBTog/configs/wconfig.py')
Configure(wband_config)

#Specifying a source for AutoOOF
AutoOOF('2253+1608')

#Let AutoOOF find a source > 3 Jy near the specified location
AutoOOF(location=Location('J2000','16:30:00','47:23:00'),flux=3.0)
Break('Examine solutions and send them to the active surface')

#AutoOOF has executed its own configuration
#Reconfigure for science observations
Configure(wband_config)
