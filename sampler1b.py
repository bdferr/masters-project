import random
import re
import os
import nltk
firsthalfdir = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col/processed'
firsthalf = next(os.walk(firsthalfdir))[2]
destinationdira = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col/more_processed'
destinationdirb = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col/fold_filenames'
firsthalfgsdir = 'C:/users/brendan/documents/library and information science/masters_project/gold-standard/first_half_untagged/processed'
firsthalfgspath = 'C:/users/brendan/documents/library and information science/masters_project/gold-standard/first_half_untagged/firsthalfgsuntagged.txt'
firsthalfgs = next(os.walk(firsthalfgsdir))[2]

if "fhgsuntagged.txt" in firsthalfgs:
    firsthalfgs.remove("fhgsuntagged.txt")
if "fhgsuntaggednames.txt" in firsthalfgs:
    firsthalfgs.remove("fhgsuntaggednames.txt")
if "firsthalftagged.txt" in firsthalf:
    firsthalf.remove("firsthalftagged.txt")
if "firsthalfuntagged.txt" in firsthalf:
    firsthalf.remove("firsthalfuntagged.txt")

##The total first half has 177 files, and the gold standard 10, has so I need samples of the following sizes from the remaining set:
sizes = [21, 42, 63, 84, 105, 126, 147, 167]


##here I try to create the gold standard test set, which needs to consist of untagged versions
##of the files in the gold standard so that its accuracy can be measured:
testset = ''
n = 1
filenamess = ''
filenamesl = []
while firsthalfgs != []:
    for choice in firsthalfgs:
        print len(firsthalfgs)
        print filenamesl
        path = firsthalfgsdir + "/" + choice
        if choice not in filenamesl:
           filenamesl.append(choice)
        if choice in firsthalf:
            firsthalf.remove(choice)
        if choice in firsthalfgs:
            firsthalfgs.remove(choice)
        ##here I make sure that the tagged version of the file is also removed from the set to be drawn from for testing,
        ##so that no file used for the test set is also used for any training fold:
        splitchoice = choice.split("_")
        shortchoice = splitchoice[:5]
        shortchoice = "_".join(shortchoice)
        tagged = shortchoice + "_tagged.txt"
        if tagged in firsthalf:
            firsthalf.remove(tagged)
        filetext = open(path).read()
        testset += filetext
        print "File number", n, "added to gold standard set"
        n += 1
tf = destinationdira + "/fhgsuntagged.txt"
with open(tf, 'w') as file:
    file.write(testset)
    print "Gold standard test set written to %s" % tf 
    file.close()
namespath = destinationdira + "/fhtestsetnames.txt"
for row in filenamesl:
    filenamess += row
    filenamess += "\n"
with open(namespath, 'w') as namesfile:
    namesfile.write(filenamess)
    print "New training set file names written to %s" % namespath

##here I create the training folds and their filename lists:
foldnum = 1
for x in sizes:
    i = 1
    filenamesl = []
    path = ''
    filetext = ''
    foldtext = ''
    while i <= x:
        choice = random.choice(firsthalf)
        path = firsthalfdir + "/" + choice
        if re.search("^.*_tagged.txt$", choice) and choice not in filenamesl and choice not in firsthalfgs:
            ##I remove the corresponding tagged file from the possibility of being selected 
            ##for training in the cross-validation, though this might be superfluous:
            filenamesl.append(choice)
            filetext = open(path).read()
            foldtext += filetext
            i += 1
    ##here I create files listing the file names in each test fold:
    namespath = destinationdirb + "/fold" + str(foldnum) + "filenames.txt"
    with open(namespath, 'w') as namesfile:
        for row in filenamesl:
            namesfile.write(row)
            namesfile.write("\n")
        print "File names for fold", foldnum, "written to %s" % namespath
        namesfile.close()
    ##here I write the text of every file in the fold to a single file:
    textpath = destinationdira + "/fold" + str(foldnum) + "text.txt"
    with open(textpath, 'w') as ftfile:
        ftfile.write(foldtext)
        print "Text for fold", foldnum, "written to %s" % textpath
	ftfile.close()
    foldnum += 1
print "All folds completed!"