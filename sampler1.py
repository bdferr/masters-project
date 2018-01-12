#This is an earlier and more convoluted version of the script I ultimately ended up using, sampler1b.py.
#I am leaving it here to show my thinking at the time.
#It refers to cross-validation, which I ultimately could not do as discussed on page 61 of the master's paper.
import random
import re
import os
import nltk
firsthalfdir = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col/processed'
firsthalf = next(os.walk(firsthalfdir))[2]
destinationdira = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col/more_processed'
destinationdirb = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/first_half_col/fold_filenames'
firsthalfgsdir = 'C:/users/brendan/documents/library and information science/masters_project/gold standard/first_half_untagged/processed'
firsthalfgspath = 'C:/users/brendan/documents/library and information science/masters_project/gold standard/first_half_untagged/firsthalfgsuntagged.txt'

##I must choose a single held-out test set of 1/9 of the files; in this case I will use 19.
##The total half has 179 files, so I need samples of the following sizes from the remaining set:
Gsizes = [20, 40, 60, 80, 100, 120, 140, 160]
##For each list, it needs to be (they need to be? if tagged and untagged are dealt with separately) broken down
##into test and training set of one pair of the following sizes:
Ltrainsizes = [17, 33, 50, 67, 83, 100, 117, 133]
Ltestsizes = [3, 7, 10, 13, 17, 20, 23, 27]
##these will be moved through using an index number:
d = 0
##do I just create one tagger beforehand like so?
##tagger = Tnt()
##now I am confused as to how to tag an entire file with nltk, although I see tagging a sentence (tag(self, data))
##and tagging a list of sentences (tagdata(self, data)) here: http://www.nltk.org/_modules/nltk/tag/tnt.html 

##here I try to create the held-out test set, which needs to consist of untagged versions
##of the files in the gold standard so that its accuracy can be measured:
testset = ''
n = 1
filenamess = ''
filenamesl = []
while n < 20:
    choice = random.choice(firsthalf)
    path = firsthalfdir + "/" + choice
    if re.search("^.*untagged.txt$", path) and choice not in filenamesl:
        filetext = open(path).read()
        filenamesl.append(choice)
        firsthalf.remove(choice)
        ##here I make sure that the tagged version of the file is also removed from the set to be drawn from,
        ##so that no file used for the held-out test set is also used for any training fold:
        splitchoice = choice.split("_")
        shortchoice = splitchoice[:5]
        shortchoice = "_".join(shortchoice)
        tagged = shortchoice + "_tagged.txt"
        firsthalf.remove(tagged)
        testset += filetext
        print("File number", n, "added to held-out set")
        n += 1
tf = destinationdira + "/heldouttext.txt"
with open(tf, 'w') as file:
    file.write(testset)
    print "Held-out test set written to %s" % tf 
    file.close()
namespath = destinationdira + "/heldoutnames.txt"
for row in filenamesl:
    filenamess += row
	filenamess += "\n"
with open(namespath, 'w') as namesfile:
    namesfile.write(filenamess)
    print "New training set file names written to %s" % namespath
    namesfile.close()

##here I create the greater folds filename lists, from which to select
##a training and test set from each fold:
foldnum = 1
for x in Gsizes:
    i = 1
    filenamesl = []
    path = ''
    while i <= x:
        choice = random.choice(firsthalf)
        path = firsthalfdir + "/" + choice
        if re.search("^.*_untagged.txt$", choice) and choice not in filenamesl:
            ##I remove the corresponding tagged file from the possibility of being selected 
            ##for training in the cross-validation, though this might be superfluous:
            splitchoice = choice.split("_")
            shortchoice = splitchoice[:5]
            shortchoice = "_".join(shortchoice)
            filenamesl.append(shortchoice)
            i += 1
    ##here I create files listing the file names in each test fold:
    namespath = destinationdirb + "/gfold" + str(foldnum) + "filenames.txt"
    with open(namespath, 'w') as namesfile:
        for row in filenamesl:
            namesfile.write(row)
            namesfile.write("\n")
        print "File names for fold", foldnum, " written to %s" % namespath
        namesfile.close()

    foldnum +=1

##here I define the set of files for random selections:
trainsource = testsource = firsthalf

##here I create the test sets for the cross-validation:
foldnum = 1
greaterfolds = next(os.walk(destinationdirb))[2]
for fold in greaterfolds:
    d = foldnum - 1
    i = 1
    j = 1
    testfilenamess = ''
    trainfilenamess = ''
    testfilenamesl = []
    trainfilenamesl = []
    foldfiles = []
    testfoldt = ''
    trainfoldt = ''
    path = ''
    namespath = ''
    choice = ''
    f = re.search(str(foldnum), fold)
    if f:
        path = destinationdirb + "/" + fold
		##this puts all the names in each name file into a list:
        with open(path, 'r') as namesfile:
            for row in namesfile:
                row = row.split("\n")
                row = "".join(row)
                foldfiles.append(row)
        while i <= Ltestsizes[d] and len(foldfiles) > 0:
            choice = random.choice(foldfiles)
            pathu = firsthalfdir + "/" + choice + "_untagged.txt"
            if choice not in testfilenamesl:
                ufile = open(pathu).read()
                testfilenamesl.append(choice)
                ##I remove the file from the possibility of being selected 
                ##for training in the cross-validation:
                if choice in foldfiles:
                    foldfiles.remove(choice)
                testfoldt += ufile
                print pathu, " written to test fold %s." % foldnum
                print i
                i += 1
        while j <= Ltrainsizes[d] and len(foldfiles) > 0:
            choice = random.choice(foldfiles)
            print choice
            print len(foldfiles)
            ##print foldfiles
            print Ltrainsizes[d]
            print j
            ##print trainfilenamesl
            patht = firsthalfdir + "/" + choice + "_tagged.txt"
            ##I was getting stuck in a loop where some files somehow ended up
            ##both in foldfiles and trainfilenamesl at the same time, so I had to do this:
            if choice in trainfilenamesl:
                trainfilenamesl.remove(choice)
            if choice not in trainfilenamesl:
                tfile = open(patht).read()
                trainfilenamesl.append(choice)
                ##I remove the corresponding tagged file from the possibility of being selected 
                ##for training in the cross-validation:
                if choice in foldfiles:
                    foldfiles.remove(choice)
                trainfoldt += tfile
                print patht, " written to training fold %s." % foldnum
                print j
                j += 1
	##here I create files listing the file names in each test and training fold:
    for row in testfilenamesl:
        testfilenamess += row + "\n"
    namespath = destinationdira + "/testfold" + str(foldnum) + "filenames.txt"
    with open(namespath, 'w') as namesfile:
        namesfile.write(testfilenamess)
        print "New test set file names written to %s" % namespath
        namesfile.close()
    for row in trainfilenamesl:
        trainfilenamess += row + "\n"
    namespath = destinationdira + "/trainfold" + str(foldnum) + "filenames.txt"
    with open(namespath, 'w') as namesfile:
        namesfile.write(trainfilenamess)
        print "New training set file names written to %s" % namespath
        namesfile.close()
    ##here I write the text for this test fold to a file:
    path = destinationdira + "/testfold" + str(foldnum) + "text.txt"
    with open(path, 'w') as textfile:
        textfile.write(testfoldt)
        print "New test set text written to %s" % path
        textfile.close()
    ##here I do the same for the training fold:
    path = destinationdira + "/trainfold" + str(foldnum) + "text.txt"
    with open(path, 'w') as textfile:
        textfile.write(trainfoldt)
        print "New training set text written to %s" % path
        textfile.close()
    foldnum += 1
print "All folds completed!"
