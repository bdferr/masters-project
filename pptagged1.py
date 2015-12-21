import os
import re
##here I access all of the file names in the directory for the first half:
mydir='C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col'
firsthalf=next(os.walk(mydir))[2]
##here I strip everything but the tokens and tags:
allu = allt = ''
for ofilename in firsthalf:
    s= ''
    u = ''
    if ofilename!='firsthalftagged.txt':
        filename = mydir + "/" + ofilename
        print("processing %s \n" % filename)
        with open(filename,'r') as f:
            for row in f:
                ##if it is a blank row, it will not need much processing:
                m = re.match("^\s*\n$", row)
                if m:
                    s=s+"\n"
                else:
                    row = row.split("\t")
                    ##print("Old row: ", row)
                    untagged = row[1] + "\n"
                    tagged = row[1] + "\t" + row[3] + "\n"
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
                    print("New row in %s" % filename, ": ", row)
                ##print m
        ##here I write each new tagged file to its own new file:
        newfilenamet = mydir + '/processed/' + ofilename.split(".")[0] + "_tagged.txt"
        print ("New tagged file written to %s " % newfilenamet)
        with open("%s" % newfilenamet,'w') as nf:
            nf.write(s)
        print("File written to %s" % newfilenamet)
        nf.close()
        allt = allt + s
        ##here I write each new untagged file to its own new file:
        newfilenameu = mydir + '/processed/' + ofilename.split(".")[0] + "_untagged.txt"
        with open("%s" % newfilenameu,'w') as nf:
            nf.write(u)
        print("New untagged file written to %s" % newfilenameu)
        nf.close()
        allu = allu + u
##here I write every file from that half to a single file:
endpath = mydir + '/firsthalftagged.txt'
with open('%s' % endpath,'w') as f:
    f.write(allt)
    print("Entire tagged contents of folder written to file %s" % endpath)
    f.close()
endpath = mydir + '/firsthalfuntagged.txt'
with open('%s' % endpath,'w') as f:
    f.write(allu)
    print("Entire untagged contents of folder written to file %s" % endpath)
    f.close()