#Example 1 - track 3C48 for 60 seconds using the center beam
Track('3C48', None, 60.0)

#Example 2 - track a position offset by 1 degree in elevation
Track('3C48', None, 60.0, fixedOffset=Offset('AzEl', 0.0, 1.0) )

#Example 3 - scan across the source from -1 to +1 degrees in azimuth
Track('3C48', Offset('AzEl', 2.0, 0.0), 60.0,
  fixedOffset=Offset('AzEl',-1.0, 0.0))
