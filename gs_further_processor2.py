#This script was used after the gs_preprocessor scripts for the second half of the gold standard corpus.
#It deals with the two files produced by concatenating all of the tagged and preprocessed files for one
#and all of the untagged preprocessed files for the other.
#Certain characters are corrected in the tagged file and new blank lines are added
#at the end of sentences in the untagged file.
import re
import os
gstaggedpath ='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_tagged/processed/shgstagged.txt'

#first we opened the tagged file and look at every row in it:
new = ''
with open(gstaggedpath,'r') as gs:
    rownum = 1
    for row in gs:
        #if the row consists only of white space, replace it with a newline character:
        if re.search("^\s*$", row):
            new += "\n"
            print "Blank line found at row %s!" % rownum
        else:
            r = re.search("^.*\$\.\s*$", row)
            if r:
            #If the row ends with "$.", which indicates the end of a sentence but is not how we want 
	    #to indicate that for the current purposes, replace it with "SENT" plus a newline:
                splitrow = row.split("\t")
                print splitrow
                newrow = str(splitrow[0]) + "\tSENT\n"
                new += newrow
                print "New blank line added at row", rownum, "after", str(newrow), "!"
            #otherwise change nothing:
            else:
                new += row
            print "Row", rownum, "processed!"
        rownum += 1
#this writes the newly edited tagged file to its existing location:
with open(gstaggedpath, 'w') as gs:
    gs.write(new)
    print "Edited file written to %s!" % gstaggedpath

gsuntaggedpath ='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_untagged/processed/shgsuntagged.txt'
#next we open the untagged file and look at every row in it:
new = ''
with open(gsuntaggedpath,'r') as gs:
    rownum = 1
    for row in gs:
        #if the line is just whitespace, replace it with a newline:
        if re.search("^\s*$", row):
            new += "\n"
            print "Blank line found at row %s!" % rownum
        else:
            #if the line starts with any of these characters: .!?:; followed by any other character
            #(this will probably be a newline), add a blank line after it:
            r = re.search("^[\.\!\?\:\;].$", row)
            if r:
                newrow = row + "\n"
                new += newrow
                print "New blank line added at row", rownum, "after", str(newrow), "!"
            #otherwise change nothing:
            else:
                new += row
            print "Row", rownum, "processed!"
        rownum += 1
#this writes the newly edited untagged file to its existing location:
with open(gsuntaggedpath, 'w') as gs:
    gs.write(new)
    print "Edited file written to %s!" % gsuntaggedpath
