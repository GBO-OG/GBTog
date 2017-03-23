#Peak using default settings
Peak('0137+3309')

#Peak using encoder coordinates with scans of 90' length in 30 sec
Peak('0137+3309',Offset('Encoder','00:90:00',0),
                 Offset('Encoder',0,'00:90:00'),30,'1')
