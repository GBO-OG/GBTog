from mx import DateTime

switchTime=DateTime.DateTime(2016,2,12,13,15,0) # Feb 12, 2016, 13:15 UTC

while Now() < switchTime and Now() != None:
    Track(srcA,None,60)

Track(srcB,None,600)
