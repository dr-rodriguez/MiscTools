#!/usr/bin/python

"""
David Rodriguez
Aug 22, 2012
Make a nice Aladin plot of all objects in a VOTable
"""

import sys,os
from astropy.io.votable import parse

file = sys.argv[1]

# Read in the VOTable
votable = parse(file)
t = votable.get_first_table()

ra = t.array['RA']
dec = t.array['Dec']
name = t.array['NAME']

script = "\n"

for i in range(len(ra)):
	cname = name[i]

	script += 'reset;\n'
	script += 'sync;\n'
	
	# Alternative script examples
	#script += 'get aladin(POSSI,O-DSS2),aladin(POSSII,J-DSS2),aladin(2MASS,K) '+str(rag[i])+' '+str(deg[i])+'\n'
	#script += 'get STScI(dss1),ESO(dss2),aladin(2mass,k) '+str(rag[i])+' '+str(deg[i])+'\n'
	#script += 'get aladin '+str(ra[i])+' '+str(dec[i])+'\n'
	script += 'get aladin(2mass,k) '+str(ra[i])+' '+str(dec[i])+'\n'
	script += 'sync;\n'

	#script += 'RGB @1 @2 @3;\n' #Auto generate red-green-blue images

	# Export to a file
	script += 'zoom 1 arcmin;\n'
	script += 'reticle on;\nsetconf overlays=-target;sync;\n'

	#script += 'get Simbad;\n' #Include Simbad objects

	script += 'save '+sname+'.png;\n\n'


print script

# Actually run everything
f = open('script.ajs','w')
f.write(script)
f.close()

# Change to specify correct Aladin.jar path
txt = 'java -jar /Applications/Aladin.app/Contents/Java/Aladin.jar < script.ajs'
os.system(txt)

print 'Done.'
