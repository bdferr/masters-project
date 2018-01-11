##This script deals with the results of the tagging. It takes the full list of part of speech tags
##in the tagged files, which is too long to be manageable, and puts them
##into broader categories like "noun." It provides counts for these broader categories,
##which are the only ones I used in displaying the results in tables.
import os
import re
##Here I get the file names for every file in the directory for documents which have been tagged.
dirpath = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/tnt-tagged-rows'
files = os.walk(dirpath)[2]

##This uses lists to sort the initial part of speech tags into the broader categories I need.
N = [NN, NE]
V = [VAFIN, VAIMP, VVFIN, VVIMP, VMFIN, VVINF, VAINF, VMINF, VVIZU, VVPP, VMPP, VAPP]
ART =[ART]
ADJ =[ADJA, ADJD]
P = [PPER, PRF, PPOSAT, PPOSS, PDAT, PDS, PIDAT, PIS, PIAT, PRELAT, PRELS, PWAT, PWS, PWAV, PAV]
CARD = [CARD]
ADV =[ADV]
KO = [KOUI, KOUS, KON, KOKOM]
AP = [APPO, APPR, APPRART, APZR]
I = [$,, $(, $.]
PTK = [PTKZU, PTKNEG, PTKVZ, PTKA, PTKANT]
S = [ITJ, TRUNC, XY, FM]

catlist = [N, V, ART, ADJ, P, CARD, ADV, KO, AP, I, PTK, S]
##These names are needed for the print statements later in this script
##which will inform me how many tokens of which type are found in each file:
catnames = ["N", "V", "ART", "ADJ", "P", "CARD", "ADV", "KO", "AP", "I", "PTK", "S"]

Ncount = 0
Vcount = 0
ARTcount = 0
ADJcount = 0
Pcount = 0
CARDcount = 0
ADVcount = 0
KOcount = 0
APcount = 0
Icount = 0
PTKcount = 0
Scount = 0
##This is a list of counts of parts of speech:
countlist = [Ncount, Vcount, ARTcount, ADJcount, Pcount, CARDcount, ADVcount, KOcount, APcount, Icount, PTKcount, Scount]

for file in files:
    path = dirpath + "/" + file
    with open(path, "r") as openedfile:
	    rownum = 1
	    for row in openedfile:
		    i = 0
		    for cat in catlist:
	                    ##For each row in each file, if the second element of the row, stripped of whitespace, 
	                    ##is an element in a category list, increment the count of that category.
			    if row[1].strip() in cat:
				    countlist[i] += 1
				print countlist[i] "tokens of type" catnames[i] "found in file" file
			    i += 1
        rownum += 1
