PointMapWithReference('2023+2223',       # center of map
   Offset('B1950', 1.5, 0.0, cosv=True), # 90' width
   Offset('B1950', 0.0, 1.5, cosv=True), # 90' height
   Offset('B1950', 0.5, 0.0, cosv=True), # 30' horizontal step spacing
   Offset('B1950', 0.0, 5.0, cosv=True), # 30' vertical step spacing
   Offset('J2000', 3.0, 0.0, cosv=True), # 3 degree ref offset in RA
   2, 2.0)            # ref before every 2 points, 2 second scan duration

