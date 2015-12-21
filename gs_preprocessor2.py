import os
import re
##here I access all of the file names in the directory for the second half:
taggeddir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_tagged'
secondhalfgst=next(os.walk(taggeddir))[2]
if 'shgstagged.txt' in secondhalfgst:
    secondhalfgst.remove('shgstagged.txt')
if 'shgstaggednames.txt' in secondhalfgst:
    secondhalfgst.remove('shgstaggednames.txt')
	
untaggeddir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_untagged'
secondhalfgsu=next(os.walk(untaggeddir))[2]
if 'secondhalfgsuntagged.txt' in secondhalfgsu:
    secondhalfgsu.remove('shgsuntagged.txt')
if 'shgsuntaggednames.txt' in secondhalfgsu:
    secondhalfgsu.remove('shgsuntaggednames.txt')

##here I strip everything but the tokens and tags:
all = ''
filenamesl = []
filenamess = ''
endpath = ''
for ofilename in secondhalfgst:
    s= ''
    ##print(os.getcwd())
    filename = taggeddir + "/" + ofilename	
    with open(filename,'r') as f:
        if filename not in filenamesl:
            filenamesl.append(filename)
        print "Reading rows from %s..." % filename
        for row in f:
            m = re.match("^\s*\n$", row)
            if m:
                s=s+"\n"
            else:
                row = row.split("\t")
                ##print("Old row: ", row)
                row = row[0] + "\t" + row[3]
                s=s+row
            ##print m
        all += s
    ##here I write each stripped file to its own new file:
    newfilename = taggeddir + "/processed/" + ofilename.split(".")[0] + "_tagged.txt"
    ##print "New file named ", newfilename
    with open(newfilename,'w') as nf:
        nf.write(s)
        print("File written to %s" % newfilename)
##here I write a list of the files in the order they were processed:
for row in filenamesl:
    filenamess += row
    filenamess += "\n"
names = taggeddir + "/processed/shgstaggednames.txt" 
with open(names, 'w') as namesfile:
    namesfile.write(filenamess)
    ##here I write every file from that half to a single file, which somehow doesn't work:
endpath = taggeddir + "/processed/shgstagged.txt"
with open(endpath,'w') as f:
    f.write(all)
    print("All tagged files written to file %s" % endpath)

##here I deal with the untagged files:
all=''
filenamesl = []
filenamess = ''
endpath = ''
for ofilename in secondhalfgsu:
    s=''
    filename = untaggeddir + "/" + ofilename
    with open(filename,'r') as f:
        if filename not in filenamesl:
            filenamesl.append(filename)
        print "Reading rows from %s..." % filename
        for row in f:
            s=s+row
        all += s
    ##here I write each stripped file to its own new file:
    newfilename = untaggeddir + "/processed/" + ofilename.split(".")[0] + "_untagged.txt"
    with open(newfilename,'w') as nf:
        nf.write(s)
        print("File written to %s" % newfilename)
##here I write a list of the files in the order they were processed to a file:
for row in filenamesl:
    filenamess += row
    filenamess += "\n"
names =	untaggeddir + "/processed/shgsuntaggednames.txt"
with open(names, 'w') as namesfile:
    namesfile.write(filenamess)
##here I write every file from that half to a single file:
endpath = untaggeddir + "/processed/shgsuntagged.txt"
with open(endpath,'w') as f:
    f.write(all)
    print "All untagged files written to %s" % f