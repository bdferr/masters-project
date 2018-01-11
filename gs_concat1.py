##This file concatenates all of the tagged and processed files from the first half of the corpus
##into a single file, then does the same in a second file for the untagged and processed files.
import os
import re
##here I access all of the file names in the already processed directory for the first half:
mydir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/first_half_tagged/processed'
firsthalf=next(os.walk(mydir))[2]
allt = ''
s = ''
if 'firsthalfgstagged.txt' in firsthalf:
    firsthalf.remove('firsthalfgstagged.txt')
##here I add the contents of each of these files to a single variable:
for ofilename in firsthalf:
    filename = mydir + "/" + ofilename
    s = open(filename, 'r').read()
    print("processing %s \n" % filename)
    allt += s
##here I write the value of the variable to a file:
endpath = mydir + "/firsthalfgstagged.txt"
with open("%s" % endpath,'w') as f:
    f.write(allt)
    print("Entire tagged contents of folder written to file %s" % endpath)
    f.close()

mydir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/first_half_untagged/processed'
firsthalf=next(os.walk(mydir))[2]
allu = ''
u = ''
if 'firsthalfgsuntagged.txt' in firsthalf:
    firsthalf.remove('firsthalfgsuntagged.txt')
##here I add the contents of each of these files to a single variable:
for ofilename in firsthalf:
    filename = mydir + "/" + ofilename
    u = open(filename, 'r').read()
    print("processing %s \n" % filename)
    allu += u
##here I write the value of the variable to a file:
endpath = mydir + "/firsthalfgsuntagged.txt"
with open("%s" % endpath,'w') as f:
    f.write(allu)
    print("Entire untagged contents of folder written to file %s" % endpath)
    f.close()
