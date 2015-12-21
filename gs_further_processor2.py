import re
import os
gstaggedpath ='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_tagged/processed/shgstagged.txt'

new = ''
with open(gstaggedpath,'r') as gs:
    rownum = 1
    for row in gs:
        if re.search("^\s*$", row):
            new += "\n"
            print "Blank line found at row %s!" % rownum
        else:
            r = re.search("^.*\$\.\s*$", row)
            if r:
                splitrow = row.split("\t")
                print splitrow
                newrow = str(splitrow[0]) + "\tSENT\n"
                new += newrow
                print "New blank line added at row", rownum, "after", str(newrow), "!"
            else:
                new += row
            print "Row", rownum, "processed!"
        rownum += 1
with open(gstaggedpath, 'w') as gs:
    gs.write(new)
    print "Edited file written to %s!" % gstaggedpath

gsuntaggedpath ='C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_untagged/processed/shgsuntagged.txt'

new = ''
with open(gsuntaggedpath,'r') as gs:
    rownum = 1
    for row in gs:
        if re.search("^\s*$", row):
            new += "\n"
            print "Blank line found at row %s!" % rownum
        else:
            r = re.search("^[\.\!\?\:\;].$", row)
            if r:
                newrow = row + "\n"
                new += newrow
                print "New blank line added at row", rownum, "after", str(newrow), "!"
            else:
                new += row
            print "Row", rownum, "processed!"
        rownum += 1
with open(gsuntaggedpath, 'w') as gs:
    gs.write(new)
    print "Edited file written to %s!" % gsuntaggedpath