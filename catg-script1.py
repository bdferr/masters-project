import os
import re
##there is nothing currently in this folder:
dirpath = 'C:/users/brendan/documents/library and information science/masters_project/germanc-corpus/tnt-tagged-rows'
files = os.walk(dirpath)[2]

##are the one-item lists really necessary? At least they remind me that those categories
##really do contain only one item.
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
##can I keep a list of items which are actually variables like this?
countlist = [Ncount, Vcount, ARTcount, ADJcount, Pcount, CARDcount, ADVcount, KOcount, APcount, Icount, PTKcount, Scount]

for file in files:
    path = dirpath + "/" + file
    with open(path, "r") as openedfile:
	    rownum = 1
	    for row in openedfile:
		    i = 0
		    for cat in catlist:
			    ##increment a count for this list by one somehow
			    if row[1].strip() in cat:
				    countlist[i] += 1
				print countlist [i] "tokens of type" catnames[i] "found in file" file
			    i += 1
        rownum += 1