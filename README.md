# MiscTools

This is a place for me to store the variety of tools I create in Python, or any other programming language.

# File List

* imagealadin.py -- tool to read in a VOTable of astronomical sources 
and automatically generate finder charts using the Aladin software. 
Requires [Aladin Desktop](http://aladin.u-strasbg.fr/java/nph-aladin.pl?frame=downloading) 
and some editing to work for your setup.

* aladinvo.py -- tool to transmit object coordinates to Aladin. 
This is writen to be used within [TOPCAT](http://www.star.bris.ac.uk/~mbt/topcat/) so that clicking a source will automatically load up an 
image and Simbad information for the target.