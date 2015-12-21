import os
import re
##here I access all of the file names in the already processed directory for the second half:
mydir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_tagged/processed'
secondhalf=next(os.walk(mydir))[2]
allt = ''
allu = ''
s = ''
u = ''
if 'secondhalfgstagged.txt' in secondhalf:
    secondhalf.remove('secondhalfgstagged.txt')
for ofilename in secondhalf:
    filename = mydir + "/" + ofilename
    s = open(filename, 'r').read()
    print("processing %s \n" % filename)
    allt += s
##here I write every tagged file from that half to a single file:
endpath = mydir + "/secondhalfgstagged.txt"
with open("%s" % endpath,'w') as f:
    f.write(allt)
    print("Entire tagged contents of folder written to file %s" % endpath)
    f.close()

mydir='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_untagged/processed'
secondhalf=next(os.walk(mydir))[2]
allt = ''
allu = ''
s = ''
u = ''
if 'secondhalfgsuntagged.txt' in secondhalf:
    secondhalf.remove('secondhalfgsuntagged.txt')
for ofilename in secondhalf:
    filename = mydir + "/" + ofilename
    u = open(filename, 'r').read()
    print("processing %s \n" % filename)
    allu += u
##here I write every untagged file from that half to a single file:
endpath = mydir + "/secondhalfgsuntagged.txt"
with open("%s" % endpath,'w') as f:
    f.write(allu)
    print("Entire untagged contents of folder written to file %s" % endpath)
    f.close()