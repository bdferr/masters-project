#This script is very similar in purpose to pptagged2.py, except that it
#deals with a few files which have a special arrangement of columns.
#The tokens in these files are in a different column than in the others,
#but the processing is the same except that it does not produce concatenated files
#including every new tagged and untagged file, which I believe turned out to be unnecessary.
#It simply produces new tagged and untagged versions
#of each file, which is what the tagger needed for training and testing respectively.
#It also ensures that these have blank lines at the end of every sentence, 
#which again was required by the tagger.
import os
import re
#Here I access all of the file names in the directory for the second half:
subdir='C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/second_half_col/special/'
specialset=next(os.walk(subdir))[2]
#Here I strip everything but the tokens and tags:
for ofilename in specialset:
    s= ''
    u = ''
    filename = subdir + ofilename
    print("processing %s" % filename)
    with open(filename,'r') as f:
        for row in f:
            #If the row is only whitespace, replace it with a newline:
            m = re.match("^\s*\n$", row)
            if m:
                s=s+"\n"
            else:
                #Otherwise strip out everything but the token and tag for the tagged version
                #and everything but the token for the untagged version:
                row = row.split("\t")
                untagged = row[6] + "\n"
                tagged = row[6] + "\t" + row[3] + "\n"
                #This checks for sentence-ending tags, making sure each is followed by a break:
                mt = re.match("^.*\$\.$", tagged)
                mtt = re.match("^/.*SENT/.*$", tagged)
                if mt or mtt:
                    s = s + tagged + "\n"
                else:
                    s = s + tagged
                #This checks for sentence-ending punctuation, making sure it is followed by a break:
                    mu = re.match("^[\.?!:;]\s*$", untagged)
                if mu:
                    u = u + untagged + "\n"
                else:
                    u = u + untagged
                print("Old row in %s" % filename, ": ", row)
    #Here I write each new tagged file to its own new file:
    newfilenamet = subdir + ofilename.split(".")[0] + "_tagged.txt"
    with open(newfilenamet,'w') as nf:
        nf.write(s)
    print("New tagged file written to %s" % newfilenamet)
    nf.close()
    #Here I write each new untagged file to its own new file:
    newfilenameu = subdir + ofilename.split(".")[0] + "_untagged.txt"
    with open(newfilenameu,'w') as nf:
        nf.write(u)
    print("New untagged file written to %s" % newfilenameu)
    nf.close()
