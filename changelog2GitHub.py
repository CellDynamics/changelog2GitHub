import xml.etree.ElementTree as ET

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

typeconvert = {'update': 'U', 'fix': 'B', 'add':'F'}
changelog = '/home/baniuk/Documents/Repos/QuimP-env/QuimP/src/changes/changes.xml'

e = ET.parse(changelog).getroot()

# get latest release child assuming that it is first on list

releases = list(list(e)[1])
latest_issues = list(releases[0])

print bcolors.OKBLUE + "Doing " + str(latest_issues.__len__()) + " entries for tag " + releases[0].get("version") + bcolors.ENDC
print 
print bcolors.FAIL+"---->"+bcolors.ENDC

print "This release fixes:"
print
for texts in latest_issues:
	issue = texts.get("issue")
	type = texts.get("type")
	print " * __["+typeconvert.get(type)+"]__ #" + str(issue) + " " +texts.text.rstrip().lstrip() 
print
print "_Legend: [B] - bugfix, [F] - feature added, [U] - update or enhancement_"
print bcolors.FAIL+"<----"+bcolors.ENDC