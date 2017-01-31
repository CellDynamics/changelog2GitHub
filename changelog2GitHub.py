import xml.etree.ElementTree as ET

e = ET.parse('/home/baniuk/Documents/Repos/QuimP-env/QuimP/src/changes/changes.xml').getroot()

# get latest release child assuming that it is first on list
latest_release = list(list(list(e)[1])[0])

print "Doing " + str(latest_release.__len__()) + " entries"
for texts in list(list(list(e)[1])[0]):
	issue = texts.get("issue")
	print texts.text.rstrip().lstrip() + " Fixes #" + str(issue) 