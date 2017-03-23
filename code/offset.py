start_location = Location('J2000','12:00:00','45:00:00')
offset1        =   Offset('J2000','00:04:00','01:00:00',cosv=False)
offset2        =   Offset('J2000', 2.0      , 2.0      ,cosv=False)
offset3        = offset1 + offset2

loc1 = start_location + offset1  #loc1 (RA,Dec) = (12:04:00, 45:00:00)
loc2 = start_location - offset2  #loc2 (RA,Dec) = (11:52:00, 43:00:00)
loc3 = start_location + offset3  #loc3 (RA,Dec) = (12:12:00, 48:00:00)
print 'RA,Dec of loc3 = (%s,%s)'%(loc3.GetH(),loc3.GetV())
