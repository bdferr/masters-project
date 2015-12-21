import os
import re
##here I access all of the file names in the directory for the first half:
##os.path.isdir(mydirname),os.path.isfile(myfilename),os.path.exists(mysomethingname)
mydir='C:/users/brendan/documents/library and information science/masters_project/gold standard/second_half_untagged'
secondhalfgs=next(os.walk(mydir))[2]

all = ''
for ofilename in secondhalfgs:
    s= ''
    if ofilename!='secondhalfgsuntagged.txt':
        filename = 'C:/users/brendan/documents/library and information science/masters_project/gold standard/second_half_untagged/' + ofilename
        print("processing %s \n" % filename)
        ##Here I check to see if each line consists of . plus a space character, and if so add another newline after it:
        with open(filename,'r') as f:
            for token in f:
                if re.search("^[.!?]\s\n$", token):
                    s = s + token + "\n"
                    print("New row in %s" % filename, ": ", token)
                else:
                    s = s + token
        ##here I write each altered file to its own new file:
        newfilename = 'C:/users/brendan/documents/library and information science/masters_project/gold standard/second_half_untagged/processed/' + ofilename.split(".")[0] + "_untagged.txt"
        ##print ("New file named ", newfilename)
        with open("%s" % newfilename,'w') as nf:
            nf.write(s)
        print("File written to C:/users/brendan/documents/library and information science/masters_project/gold standard/second_half_untagged/processed/%s" % newfilename)
        nf.close()
        all = all + s
##here I write every file from that half to a single file:
with open("C:/users/brendan/documents/library and information science/masters_project/gold standard/second_half_untagged/secondhalfgsuntagged.txt",'w') as f:
    f.write(all)
    print("Entire contents of folder written to file C:/users/brendan/documents/library and information science/masters_project/gold standard/second_half_untagged/secondhalfuntagged.txt")
    f.close()