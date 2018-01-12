#In this script I check every file in the first half of the gold standard corpus, untagged,
#to add a blank row after the end of every sentence.
#This was necessary for the tagger.
import os
import re
#here I access all of the file names in the directory for the first half of the corpus, untagged:
mydir='C:/users/brendan/documents/library and information science/masters_project/gold standard/first_half_untagged'
firsthalfgs=next(os.walk(mydir))[2]

all = ''
for ofilename in firsthalfgs:
    s= ''
    if ofilename!='firsthalfgsuntagged.txt':
        filename = 'C:/users/brendan/documents/library and information science/masters_project/gold standard/first_half_untagged/' + ofilename
        print("processing %s \n" % filename)
        #Here I check to see if each line consists of a period, exclamation point or question mark
        #plus a space character and a newline character, and if so add another newline after it:
        with open(filename,'r') as f:
            for token in f:
                if re.search("^[.!?]\s\n$", token):
                    s = s + token + "\n"
                    print("New row in %s" % filename, ": ", token)
                else:
                    s = s + token
        #here I write each altered file to its own new file:
        newfilename = 'C:/users/brendan/documents/library and information science/masters_project/gold standard/first_half_untagged/processed/' + ofilename.split(".")[0] + "_untagged.txt"
        with open("%s" % newfilename,'w') as nf:
            nf.write(s)
        print("File written to %s" % newfilename)
        nf.close()
        all = all + s
#here I write every file from the first half to a single file:
with open("C:/users/brendan/documents/library and information science/masters_project/gold standard/first_half_untagged/firsthalfgsuntagged.txt",'w') as f:
    f.write(all)
    print("Entire contents of folder written to file C:/users/brendan/documents/library and information science/masters_project/gold standard/first_half_untagged/firsthalfuntagged.txt")
    f.close()
