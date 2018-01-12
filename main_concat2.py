#This script concatenates every untagged processed file from the second half of the non-gold-standard corpus
#into a single file, and does the same to a separate document for the tagged files.
import os
import re
#here I access all of the file names in the already processed directory for the second half:
mydir='C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/second_half_col/processed'
secondhalf=next(os.walk(mydir))[2]
allt = ''
allu = ''
s = ''
u = ''
#If the file ends in "untagged.txt" its contents are added to one variable for untagged files,
#and if not, to another for tagged files.
for ofilename in secondhalf:
    #This line excludes already concatenated files that might be in the folder:
    if ofilename!='secondhalftagged.txt' and ofilename!="secondhalfuntagged.txt":
        if re.search("^.*untagged.txt$", ofilename):
            filename = mydir + "/" + ofilename
            u = open(filename, 'r').read()
            print("processing %s \n" % filename)
            allu += u
        else:
            filename = mydir + "/" + ofilename
            s = open(filename, 'r').read()
            print("processing %s \n" % filename)
            allt += s

#here I write untagged every file from that half to a single file:
endpath = mydir + "/secondhalfuntagged.txt"
with open("%s" % endpath,'w') as f:
    f.write(allu)
    print("Entire untagged contents of folder written to file %s" % endpath)
    f.close()
#here I write tagged every file from that half to a single file:
endpath = mydir + "/secondhalftagged.txt"
with open("%s" % endpath,'w') as f:
    f.write(allt)
    print("Entire tagged contents of folder written to file %s" % endpath)
    f.close()
