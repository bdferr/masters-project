##This script edits both the tagged and untagged files in the first half of the gold standard corpus.
##It strips everything but the tokens and part of speech tags from the tagged files
##and produces text files listing both the tagged and untagged files
##in the order they were processed.
##It finally concatenates every processed file into a single file for the tagged
##and another file for the untagged files.
import os
import re
##here I access all of the file names in the directory for the tagged first half of the gold standard corpus:
taggeddir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/first_half_tagged'
firsthalfgst=next(os.walk(taggeddir))[2]
if 'firsthalfgstagged.txt' in firsthalfgst:
    firsthalfgst.remove('fhgstagged.txt')
if 'fhgstaggednames.txt' in firsthalfgst:
    firsthalfgst.remove('fhgstaggednames.txt')

##here I do the same for the untagged first half:	
untaggeddir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/first_half_untagged'
firsthalfgsu=next(os.walk(untaggeddir))[2]
if 'firsthalfgsuntagged.txt' in firsthalfgsu:
    firsthalfgsu.remove('fhgsuntagged.txt')
if 'fhgsuntaggednames.txt' in firsthalfgsu:
    firsthalfgsu.remove('fhgsuntaggednames.txt')

##here I strip everything but the tokens and tags from every line of every file in the tagged first half:
all = ''
filenamesl = []
filenamess = ''
endpath = ''
for ofilename in firsthalfgst:
    s= ''
    filename = taggeddir + "/" + ofilename
    with open(filename,'r') as f:
	##this adds each file name to a list of files as it is accessed:
        if filename not in filenamesl:
            filenamesl.append(filename)
        print "Reading rows from %s..." % filename
        for row in f:
	    ##if a row consists of just whitespace, replace it with a newline (this will show up as a blank row, no spaces or tabs):
            m = re.match("^\s*\n$", row)
            if m:
                s=s+"\n"
            else:
		##replace the row with just the first and fourth elements, i.e. just the token and the part of speech tag:
                row = row.split("\t")
                row = row[0] + "\t" + row[3]
                s=s+row
        all += s
    ##here I write each stripped file to its own new file:
    newfilename = taggeddir + "/processed/" + ofilename.split(".")[0] + "_tagged.txt"
    with open(newfilename,'w') as nf:
        nf.write(s)
        print("File written to %s" % newfilename)
##here I write a list of the files in the order they were processed to a text file:
for row in filenamesl:
    filenamess += row
    filenamess += "\n"
names = taggeddir + "/processed/fhgstaggednames.txt" 
with open(names, 'w') as namesfile:
    namesfile.write(filenamess)
    ##here I write every file from that half to a single file:
endpath = taggeddir + "/processed/fhgstagged.txt"
with open(endpath,'w') as f:
    f.write(all)
    print("All tagged files written to %s" % endpath)

##here I deal with the untagged files:
all=''
filenamesl = []
filenamess = ''
endpath = ''
for ofilename in firsthalfgsu:
    s=''
    filename = untaggeddir + "/" + ofilename
    with open(filename,'r') as f:
	##this adds each file name to a list of file names as it is accessed:
        if filename not in filenamesl:
            filenamesl.append(filename)
        print "Reading rows from %s..." % filename
        for row in f:
            s=s+row
        all += s
    ##here I write each processed file to its own new file:
    newfilename = untaggeddir + "/processed/" + ofilename.split(".")[0] + "_untagged.txt"
    with open(newfilename,'w') as nf:
        nf.write(s)
        print("File written to %s" % newfilename)
##here I write the list of the files in the order they were processed to a text file:
for row in filenamesl:
    filenamess += row
    filenamess += "\n"
names =	untaggeddir + "/processed/fhgsuntaggednames.txt"
with open(names, 'w') as namesfile:
    namesfile.write(filenamess)
##here I write every file from that half to a single file:
endpath = untaggeddir + "/processed/fhgsuntagged.txt"
with open(endpath,'w') as f:
    f.write(all)
    print "All untagged files written to %s" % f
