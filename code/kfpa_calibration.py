execfile('/home/astro-util/projects/GBTog/configs/kfpa_config.py')
Catalog(fluxcal)
Catalog(kband_pointing)
src = '3C286'          # Do not use extended 3C sources

Configure(kfpa_config) # Configure for KFPA receiver
AutoPeakFocus(src)     # Automatically slews, balances,
                       # and configures for continuum.

Configure(kfpa_config) # Reconfigure for VEGAS + KFPA using
Slew(src)              # the same configuration you would use
Balance()              # for your science observations....

Nod(src, '3', '7', scanDuration=30.0) # This combination covers all
Nod(src, '2', '6', scanDuration=30.0) # 7 beams - edit as necessary
Nod(src, '4', '1', scanDuration=30.0) # for other beam configurations.
Nod(src, '1', '5', scanDuration=30.0)
