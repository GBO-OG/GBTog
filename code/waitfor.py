#Wait for 15:13 LST
WaitFor('15:13:00 LST')

#Wait until source is above 10 deg elevation
WaitFor(Horizon(10.0).GetRise('1532+3421'))

#Wait for the Sun to set below 5 deg elevation
WaitFor(Horizon(5.0).GetSet('Sun'))
