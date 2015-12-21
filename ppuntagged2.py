
##here I access the second half:
mydir='C:/users/brendan/documents/library_and_information_science/masters_project/germanc-corpus/second_half_col'
secondhalf=next(os.walk(mydir))[2]
##again I strip out the columns other than the second, to produce a simple untagged file:
all=''
for filename in secondhalf:
    if filename!='secondhalfuntagged.txt':
        print("processing %s \n"%filename)
        with open(filename,'r') as f:
            for row in f:
                row = row.split("\t")
                row = row[1]
                s=s+row
            all=all+s
    ##here I write each stripped file to its own new file:
    newfilename = filename.split(".")[0] + "untagged.txt"
    with open("newfilename",'w') as nf:
        nf.write(s)
##here I write every file from that half to a single file:
with open('C:/users/brendan/documents/library_and_information_science/masters_project/germanc-corpus/second_half_col/secondhalfuntagged.txt','w') as f:
    f.write(all)