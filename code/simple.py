#load the configurations file
execfile('/mypath/myconfigurations.txt')

# load catalogs file
Catalog('/mypath/mycatalog.cat')

# configure the GBT
Configure(myconfig)

# slew to the source
Slew('B0329+54')

# balance the IF system
Balance()

# now observe the source for ten minutes
Track('B0329+54',None,600)
