#!/usr/bin/python
"""changelog2GitHub.py

This simple tool converts changelog from maven-changes-plugin
to Markdown format which is then displayed.

Only last release tag (first in xml file) is processed,
"""

import xml.etree.ElementTree as ET
import sys

class bcolors:
    OKBLUE = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

typeconvert = {	'update': 'U',
				'fix': 'B',
				'add':'F'}

if len(sys.argv)!=2:
	print("Wrong number of arguments")
	print("changelog2GitHub.py /path/to/changes.xml")
	exit(1)

# get file name
changelog = sys.argv[1]

e = ET.parse(changelog).getroot()

# get latest release child assuming that it is first on list
releases = list(list(e)[1])
latest_issues = list(releases[0]) # list of issues

print(bcolors.OKBLUE + bcolors.BOLD + "Doing " + str(latest_issues.__len__()) + " entries for tag " + releases[0].get("version") + bcolors.ENDC)
print 
print(bcolors.FAIL+"---->"+bcolors.ENDC)

print("This release fixes:")
print
for texts in latest_issues:
	issue = texts.get("issue")
	type = texts.get("type")
	print(" * __["+typeconvert.get(type)+"]__ #" + str(issue) + " " +texts.text.rstrip().lstrip())
print
print("_Legend: [B] - bugfix, [F] - feature added, [U] - update or enhancement_")
print (bcolors.FAIL+"<----"+bcolors.ENDC)