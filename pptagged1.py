#This script deals with the first half of the non-gold-standard tagged corpus. 
#It is meant to produce a tagged and untagged version
#of each file for further processing by stripping everything but the tokens and tags for the tagged version
#and everything but the token for the untagged version. This was the format needed by the tagger.
import os
import re
#here I access all of the file names in the directory for the first half of the non-gold-standard corpus:
mydir='C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col'
firsthalf=next(os.walk(mydir))[2]
#here I initialize variables and access every row from every file:
allu = allt = ''
for ofilename in firsthalf:
    s= ''
    u = ''
    #This excludes already completed concatenated files if they are already in that folder;
    #this means I can run the script more than once without the result getting larger
    #with more duplicates of the same content each time. This might not have been necessary in this context
    #but I am leaving it here anyway to show my thinking at the time:
    if ofilename != 'firsthalftagged.txt' and ofilename != 'firsthalfuntagged.txt':
        filename = mydir + "/" + ofilename
        print("processing %s \n" % filename)
        with open(filename,'r') as f:
            for row in f:
                #If the row consists of only whitespace, I replace it with a newline:
                m = re.match("^\s*\n$", row)
                if m:
                    s=s+"\n"
                else:
                    #Otherwise, produce a tagged version of it consisting of just the token and tag,
                    #plus an untagged version consisting of just the token.
                    row = row.split("\t")
                    untagged = row[1] + "\n"
                    tagged = row[1] + "\t" + row[3] + "\n"
                    #This checks for sentence ending tags and ensures all are followed by blank rows:
                    mt = re.match("^.*\$\.$", tagged)
                    mtt = re.match("^/.*SENT/.*$", tagged)
                    if mt or mtt:
                        s = s + tagged + "\n"
                    else:
                        s = s + tagged
                    #This searches for sentence ending punctuation and does the same:
                    mu = re.match("^[\.?!:;]\s*$", untagged)
                    if mu:
                        u = u + untagged + "\n"
                    else:
                        u = u + untagged
                    print("New row in %s" % filename, ": ", row)
        #Here I write each new tagged file to its own new file, now labeled as processed:
        newfilenamet = mydir + '/processed/' + ofilename.split(".")[0] + "_tagged.txt"
        print ("New tagged file written to %s " % newfilenamet)
        with open("%s" % newfilenamet,'w') as nf:
            nf.write(s)
        print("File written to %s" % newfilenamet)
        nf.close()
        allt = allt + s
        ##here I do the same for each new untagged file:
        newfilenameu = mydir + '/processed/' + ofilename.split(".")[0] + "_untagged.txt"
        with open("%s" % newfilenameu,'w') as nf:
            nf.write(u)
        print("New untagged file written to %s" % newfilenameu)
        nf.close()
        allu = allu + u
#Here I concatenate every newly processed tagged file into a single file:
endpath = mydir + '/firsthalftagged.txt'
with open('%s' % endpath,'w') as f:
    f.write(allt)
    print("Entire tagged contents of folder written to file %s" % endpath)
    f.close()
#Here I do the same for every new untagged file:
endpath = mydir + '/firsthalfuntagged.txt'
with open('%s' % endpath,'w') as f:
    f.write(allu)
    print("Entire untagged contents of folder written to file %s" % endpath)
    f.close()
