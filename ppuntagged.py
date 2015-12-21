##to make a script executable, the command is chmod 755 <nameofscript>.

##here I access all of the file names in the directory:
import os
import re
##mydir='C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col'
sourcedir = 'C:/users/brendan/documents/library and information science/masters_project/gold-standard/germanc_gs_columns'
destdir = 'C:/users/brendan/documents/library and information science/masters_project/gold-standard/first_half_untagged'

##firsthalf=next(os.walk(mydir))[2]
##if 'firsthalfuntagged.txt' in firsthalf:
##    firsthalf.remove('firsthalfuntagged.txt')

##here I attempt to strip each file in the first half
##of everything except the original tokens (second column):
all=''
ofilename = "/LETT_P1_NoD_1672_Guericke_GS.txt"
filename = sourcedir + ofilename
s=''
print("processing %s \n"%filename)
with open(filename,'r') as f:
    rownum = 1
    for row in f:
        if re.search("^\s*$", row):
            s += "\n"
            print "Blank line found at row %s!" % rownum
        else:
            row = row.split("\t")
            row = row[1] + "\n"
            s=s+row
        rownum += 1
##    all=all+s    
##here I write each stripped file to its own new file:
newfilename = destdir + ofilename
with open(newfilename,'w') as nf:
    nf.write(s)
    print "Edited file written to %s" % newfilename
##for filename in firsthalf:
##here I write every file from that half to a single file:
'''
endpath = mydir + "/processed/firsthalfuntagged.txt"
with open(endpath,'w') as f:
    f.write(all)
    print "All files written to %s" % endpath
'''