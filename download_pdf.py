#!/usr/bin/python
#
# Attempts to downlad PDF files as declared in the JSON files.
#
# The script will ask for a path to a PDF directory and will download any PDF
# file with the same name as our JSON files (with substituted extension) that
# is missing from the target directory.


import os
import json
import requests


_json_dirs = ['CDC', 'WHO']


if '__main__' == __name__:
	pdf_dir = None
	
	while pdf_dir is None or not os.path.exists(pdf_dir):
		pdf_dir = raw_input("Path to PDF directory: ")
	
	# loop all our JSON directories
	for d in _json_dirs:
		print "->  Reading %s" % d
		
		for f in os.listdir(d):
			parts = os.path.splitext(f)
			if '.json' == parts[1]:
				pdf_file = os.path.join(pdf_dir, "%s.pdf" % parts[0])
				
				# do we have a similarly named PDF?
				if not os.path.exists(pdf_file):
					print '-->  Missing PDF: "%s.pdf"' % parts[0]
					
					# read the JSON file
					with open(os.path.join(d, f), 'r') as handle:
						doc = json.load(handle)
						src = doc.get('source')
						
						# download
						if src is not None:
							print "-->  Downloading from %s" % src
							r = requests.get(src)
							if 200 == r.status_code:
								with open(pdf_file, 'wb') as pdf:
									pdf.write(r.content)
								print "-->  Saved"
							else:
								print "xx>  Failed to download: %d" % r.status_code
						else:
							print "xx>  No source specified, cannot download"

		print "->  Done"
