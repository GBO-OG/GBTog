execfile('/home/astro-util/projects/GBTog/configs/tp_config.py')
Configure(tp_config) #Execute the desired configuration
Slew('3C286')  #Slew so that you may balance 'on-source'
Balance() #Balance the IF and devices for your configuration