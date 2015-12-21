## here I give each of the files a place in an array
## so that it can be referred to by its index number:

import random

firsthalf = open('C:/users/brendan/documents/library_and_information_science/masters_project/first_half_names.txt', 'r')
firstlist = []
for row in firsthalf:
	firstlist.append(row)
for row in firstlist:
	print row
firsthalf.close()
	
secondlist = []
secondhalf = open('C:/users/brendan/documents/library_and_information_science/masters_project/second_half_names.txt', 'r')
for row in secondhalf:
	secondlist.append(row)
for row in secondlist:
	print row

##should each successive size include all the files from the previous size? it does not matter;
##you can just choose 9 sets in one division and just use 1, 1+2, 1+2+3, etc.
##choose a single test set
##Here I make random selections of items from each list, although this is just the filenames so far:

##I need samples of the following sizes from the first list: 22, 44, 66, 88, 110, 132, 154
##and test sets of the following sizes: 2, 4, 7, 9, 11, 13, 15
selection = []
testset = []
i = 0
ts = 0
while i < 22:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(firstlist[id])
	i +=1
	##fix the following; 
while ts < 2:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]
	
selection = []
testset = []
i = 0
ts = 0
while i < 44:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(firstlist[id])
	i +=1
while ts < 4:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i < 66:
	id = random.randrange(0, range(len(firstlist)-1))
	selection.append(firstlist[id])
	i +=1
while ts < 6:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i < 88:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(firstlist[id])
	i +=1
while ts < 9:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i < 110:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(firstlist[id])
	i +=1
while ts < 11:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i < 132:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(firstlist[id])
	i +=1
while ts < 13:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i < 154:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(firstlist[id])
	i +=1
while ts < 15:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

##I need samples of the following sizes from the second list: 20, 40, 60, 80, 100, 120, 140
##and test sets of the following sizes: 2, 4, 6, 8, 10, 12, 14

selection = []
testset = []
i = 0
ts = 0
while i <20:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(secondlist[id])
	i +=1
while ts < 2:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]
	
selection = []
testset = []
i = 0
ts = 0
while i <40:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(secondlist[id])
	i +=1
while ts < 4:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i <60:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(secondlist[id])
	i +=1
while ts < 6:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i <80:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(secondlist[id])
	i +=1
while ts < 8:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i <100:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(secondlist[id])
	i +=1
while ts < 10:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i <120:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(secondlist[id])
	i +=1
while ts < 12:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i <140:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(secondlist[id])
	i +=1
while ts < 14:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]

selection = []
testset = []
i = 0
ts = 0
while i <160:
	id = random.randrange(0, len(firstlist)-1)
	selection.append(secondlist[id])
	i +=1
while ts < 16:
	id = random.randrange(0, len(selection)-1)
	testset.append(selection[id])
	ts += 1
##[insert tagger commands here]