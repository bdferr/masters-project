import random
import re
import os
import nltk
shdir = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/second_half_col/processed'
secondhalf = next(os.walk(shdir))[2]
destinationdira = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/second_half_col/more_processed'
destinationdirb = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/second_half_col/fold_filenames'
shgsdir = 'C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_untagged/processed'
shgspath = 'C:/users/brendan/documents/library and information science/masters_project/gold-standard/second_half_untagged/shgsuntagged.txt'
shgs = next(os.walk(shgsdir))[2]

if "shgsuntagged.txt" in shgs:
    shgs.remove("shgsuntagged.txt")
if "shgsuntaggednames.txt" in shgs:
    shgs.remove("shgsuntaggednames.txt")
if "secondhalftagged.txt" in secondhalf:
    secondhalf.remove("secondhalftagged.txt")
if "secondhalfuntagged.txt" in secondhalf:
    secondhalf.remove("secondhalfuntagged.txt")

##The total second half has 159 files, and the gold standard 14, has so I need samples of the following sizes from the remaining set:
sizes = [18, 36, 54, 72, 90, 108, 126, 144]
##now I am confused as to how to tag an entire file with nltk, although I see tagging a sentence (tag(self, data))
##and tagging a list of sentences (tagdata(self, data)) here: http://www.nltk.org/_modules/nltk/tag/tnt.html 

##here I try to create the gold standard test set, which needs to consist of untagged versions
##of the files in the gold standard so that its accuracy can be measured:
testset = ''
n = 1
filenamess = ''
filenamesl = []
while shgs != []:
    choice = random.choice(shgs)
    print len(shgs)
    print filenamesl
    path = shgsdir + "/" + choice
    if choice not in filenamesl:
        filenamesl.append(choice)
        if choice in secondhalf:
            secondhalf.remove(choice)
        if choice in shgs:
            shgs.remove(choice)
        ##here I make sure that the tagged version of the file is also removed from the set to be drawn from for testing,
        ##so that no file used for the test set is also used for any training fold:
        splitchoice = choice.split("_")
        shortchoice = splitchoice[:5]
        shortchoice = "_".join(shortchoice)
        tagged = shortchoice + "_tagged.txt"
        if tagged in secondhalf:
            secondhalf.remove(tagged)
        filetext = open(path).read()
        testset += filetext
        print "File number", n, "added to gold standard set"
        n += 1
tf = destinationdira + "/secondhalfgsuntagged.txt"
with open(tf, 'w') as file:
    file.write(testset)
    print "Gold standard test set written to %s" % tf
    file.close()
namespath = destinationdira + "/secondhalftestsetnames.txt"
for row in filenamesl:
    filenamess += row
    filenamess += "\n"
with open(namespath, 'w') as namesfile:
    namesfile.write(filenamess)
    print "New training set file names written to %s" % namespath
    namesfile.close()

##here I create the training folds and their filename lists:
foldnum = 1
for x in sizes:
    i = 1
    filenamesl = []
    path = ''
    filetext = ''
    foldtext = ''
    while i <= x:
        choice = random.choice(secondhalf)
        path = shdir + "/" + choice
        if re.search("^.*_tagged.txt$", choice) and choice not in filenamesl and choice not in shgs:
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
    textpath = destinationdira + "/shfold" + str(foldnum) + "text.txt"
    with open(textpath, 'w') as ftfile:
        ftfile.write(foldtext)
        print "Text for fold", foldnum, "written to %s" % textpath
	ftfile.close()
    foldnum += 1
print "All folds completed!"