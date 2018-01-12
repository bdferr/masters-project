#This file concatenates all of the tagged and processed files from the second half of the gold standard corpus
#into a single file, then does the same in a second file for the untagged and processed files.
import os
import re
#here I access all of the file names in the already processed directory for the tagged second half:
mydir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_tagged/processed'
secondhalf=next(os.walk(mydir))[2]
allt = ''
s = ''
if 'secondhalfgstagged.txt' in secondhalf:
    secondhalf.remove('secondhalfgstagged.txt')
#here I add the contents of each tagged file in the second half to a single variable:
for ofilename in secondhalf:
    filename = mydir + "/" + ofilename
    s = open(filename, 'r').read()
    print("processing %s \n" % filename)
    allt += s
#here I write the value of the variable to a single file:
endpath = mydir + "/secondhalfgstagged.txt"
with open("%s" % endpath,'w') as f:
    f.write(allt)
    print("Entire tagged contents of folder written to file %s" % endpath)
    f.close()
#here I access all of the file names in the already processed directory for the untagged second half:
mydir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_untagged/processed'
secondhalf=next(os.walk(mydir))[2]
allu = ''
u = '' 
if 'secondhalfgsuntagged.txt' in secondhalf:
    secondhalf.remove('secondhalfgsuntagged.txt')
#here I add the contents of each untagged file in the second half to a single variable:
for ofilename in secondhalf:
    filename = mydir + "/" + ofilename
    u = open(filename, 'r').read()
    print("processing %s \n" % filename)
    allu += u
#here I write the value of the variable to a single file:
endpath = mydir + "/secondhalfgsuntagged.txt"
with open("%s" % endpath,'w') as f:
    f.write(allu)
    print("Entire untagged contents of folder written to file %s" % endpath)
    f.close()
