import os
import re
##here I access all of the file names in the directory for the second half:
subdir='C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/second_half_col/special/'
specialset=next(os.walk(subdir))[2]
##here I strip everything but the tokens and tags:
for ofilename in specialset:
    s= ''
    u = ''
    ##print(os.getcwd())
    filename = subdir + ofilename
    print("processing %s" % filename)
    with open(filename,'r') as f:
        for row in f:
            ##if it is a blank row, it will not need much processing:
            m = re.match("^\s*\n$", row)
            if m:
                s=s+"\n"
            else:
                row = row.split("\t")
                ##print("Old row: ", row)
                untagged = row[6] + "\n"
                tagged = row[6] + "\t" + row[3] + "\n"
                ##this checks for sentence ends to make sure all are followed by breaks:
                mt = re.match("^.*\$\.$", tagged)
                mtt = re.match("^/.*SENT/.*$", tagged)
                if mt or mtt:
                    s = s + tagged + "\n"
                else:
                    s = s + tagged
                ##so does this:
                    mu = re.match("^[\.?!:;]\s*$", untagged)
                if mu:
                    u = u + untagged + "\n"
                else:
                    u = u + untagged
                print("Old row in %s" % filename, ": ", row)
            ##print m
    ##here I write each new tagged file to its own new file:
    newfilenamet = subdir + ofilename.split(".")[0] + "_tagged.txt"
    with open(newfilenamet,'w') as nf:
        nf.write(s)
    print("New tagged file written to %s" % newfilenamet)
    nf.close()
    ##here I write each new untagged file to its own new file:
    newfilenameu = subdir + ofilename.split(".")[0] + "_untagged.txt"
    with open(newfilenameu,'w') as nf:
        nf.write(u)
    print("New untagged file written to %s" % newfilenameu)
    nf.close()