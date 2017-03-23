lfcValues = {
  'local_focus_correction,Y': -7.469,           # in mm
  'localPointingOffsets,azOffset2': 9.8902e-06, # in radians
  'localPointingOffsets,elOffset': 7.27221e-05} # in radians

SetValues('Antenna', lfcValues)
SetValues('Antenna', {'state': 'prepare'})
