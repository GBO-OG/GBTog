#Configure for the Ka receiver and DCR backend...
execfile('/home/groups/ptcs/obs/turtle/configs.py')
Configure(kaband)

AutoOOF(source='2253+1608',configure=False)