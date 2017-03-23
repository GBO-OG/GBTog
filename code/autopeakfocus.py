#Configure for correct receiver at start of session...
execfile('/home/astro-util/projects/GBTog/configs/tp_config.py')
Configure(tp_config)

#Default (fully automatic)
AutoPeakFocus()
#point and focus on 3C286
AutoPeakFocus('3C286')
# find a pointing source near ra=16:30:00 dec=47:23:00
AutoPeakFocus(location=Location('J2000','16:30:00','47:23:00'))

#AutoPeakFocus has executed its own configuration
#Reconfigure for science observations
Configure(tp_config)
