c = Catalog('mycatalog.cat')
sourcenames = c.keys()
for s in sourcenames :
    if c[s]['status'] == 'waiting' :
        dwelltime = float(c[s]['sourcetime'])
        Track(s,None,dwelltime)
