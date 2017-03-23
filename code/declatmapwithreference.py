DecLatMapWithReference('CygA',            # center of map
   Offset('J2000', 2.0, 0.0, cosv=True),  # 120' width
   Offset('J2000', 0.0, 0.5, cosv=True),  #  60' height
   Offset('J2000', 0.0, 0.1, cosv=True),  #   6' column spacing
   Offset('J2000', 2.0, 0.0, cosv=True),  # 2 degree ref offset in RA
   3, 10.0)          # ref before every 3 columns, 10 second scan duration

