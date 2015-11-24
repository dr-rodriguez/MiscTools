#!/usr/bin/python

"""
Transmit information to Aladin. Can be used within TOPCAT (see instructions at end).
Requires SAMPy module
"""


import sys
from sampy import *

ra = sys.argv[1]
dec = sys.argv[2]

hub = SAMPIntegratedClient(metadata = {"samp.name":"Python SAMPy"})
hub.connect()
id = hub.getPublicId()

# Script to send to Aladin; this will grab the default image, a 2MASS K-band image, and query simbad for the target
script="reset; get aladin,simbad,aladin(2mass,k) " + ra + " " + dec

print script

# Send the script to Aladin
hub.callAll("script.aladin.send", {"samp.mtype": "script.aladin.send", "samp.params":{"script":script}})
hub.disconnect()

"""
In TOPCAT
Add a column runme as:
concat("aladinvo.py ",toString(ra)," ",toString(dec))
and then set the Activation Action to:
exec(runme)
Both TOPCAT and Aladin must have been called from the command line (not double clicking the packaged file)
"""



