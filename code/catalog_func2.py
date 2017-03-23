c = Catalog(lband_pointing)
sourcenames = c.keys()
for s in sourcenames :
    print c[s]['dec']
    if c[s]['dec'] > 20 :
        Nod(s,'1','2',120)
