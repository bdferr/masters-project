import os
import re
##here I access all of the file names in the already processed directory for the first half of the non-gold-standard corpus:
mydir='C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col/processed'
firsthalf=next(os.walk(mydir))[2]
allt = ''
allu = ''
s = ''
u = ''
##if a file name ends in "untagged.txt" its contents are added to one variable called u,
##and if not it is added to another variable called s:
for ofilename in firsthalf:
    if ofilename!='firsthalfgstagged.txt' and ofilename!="firsthalfuntagged.txt":
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
##here I write tagged every file from the first half half to a single file:
endpath = mydir + "/firsthalftagged.txt"
with open(endpath,'w') as f:
    f.write(allt)
    print("Entire tagged contents of folder written to file %s" % endpath)
    f.close()
##here I write untagged every file from the first half to a single file:
endpath = mydir + "/firsthalfuntagged.txt"
with open(endpath,'w') as f:
    f.write(allu)
    print("Entire untagged contents of folder written to file %s" % endpath)
    f.close()
