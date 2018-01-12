#I am not sure I actually used this script in the end. In any case it deals with the second half
#of the non-gold-standard tagged corpus. It is meant to produce a tagged and untagged version
#of each file for further processing by stripping everything but the tokens and tags for the tagged version
#and everything but the token for the untagged version.
import os
import re
#Here I access all of the file names in the directory for the second half:
mydir='C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/second_half_col'
secondhalf=next(os.walk(mydir))[2]
allt = allu = ''
#Here I initialize variables and access every row from every file:
for ofilename in secondhalf:
    s= ''
    u = ''
    #I am leaving this in here to show my thinking at the time;
    #if I had put the results of this script into the same folder and run it multiple times without this,
    #I would have gotten results that got larger and more full of duplicated text each time,
    #but the already concatenated files should be in a separate folder
    #according to this script, so this line to exclude them should not be necessary:
    if ofilename!='secondhalftagged.txt' and ofilename != 'secondhalfuntagged.txt':
        filename = mydir + "/" + ofilename
        print("processing %s \n" % filename)
        with open(filename,'r') as f:
            for row in f:
                #If the row has only whitespace, replace it with just a newline:
                m = re.match("^\s*\n$", row)
                if m:
                    s=s+"\n"
                else:
                    #Otherwise create a new tagged version of the row by stripping everything but the token and tag,
                    #and a new untagged version by stripping everything but the token:
                    row = row.split("\t")
                    untagged = row[1] + "\n"
                    tagged = row[1] + "\t" + row[3] + "\n"
                    #This checks for sentence ending tags to make sure all are followed by blank lines:
                    mt = re.match("^.*\$\.$", tagged)
                    mtt = re.match("^/.*SENT/.*$", tagged)
                    if mt or mtt:
                        s = s + tagged + "\n"
                    else:
                        s = s + tagged
                    #This checks for sentence ending punctuation to do the same:
                    mu = re.match("^[\.?!:;]\s*$", untagged)
                    if mu:
                        u = u + untagged + "\n"
                    else:
                        u = u + untagged
                    print("New row in %s" % filename, ": ", row)
        #Here I write each newly processed tagged file to its own new file:
        newfilenamet = mydir + '/processed/' + ofilename.split(".")[0] + "_tagged.txt"
        print ("New tagged file named ", newfilenamet)
        with open("%s" % newfilenamet,'w') as nf:
            nf.write(s)
        print("File written to %s" % newfilenamet)
        nf.close()
        allt = allt + s
        #Here I write each new untagged file to its own new file:
        newfilenameu = mydir + '/processed/' + ofilename.split(".")[0] + "_untagged.txt"
        with open("%s" % newfilenameu,'w') as nf:
            nf.write(u)
        print("New untagged file written to %s" % newfilenameu)
        nf.close()
        allu = allu + u
#Here I concatenate every newly processed tagged file to a single file:
endpath = mydir + '/secondhalftagged.txt'
with open('%s' % endpath,'w') as f:
    f.write(allt)
    print("Entire tagged contents of folder written to file %s" % endpath)
    f.close()
#Here I concatenate every new untagged file to a single file:
endpath = mydir + '/secondhalfuntagged.txt'
with open('%s' % endpath,'w') as f:
    f.write(allu)
    print("Entire untagged contents of folder written to file %s" % endpath)
    f.close()
