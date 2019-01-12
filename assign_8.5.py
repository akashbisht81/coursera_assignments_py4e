fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst=list()
for i in fh:
    lst=i.split()
    #print(lst)
    if 'From' in lst:
            word=lst[1]
            print(word)
            count=count+1
    else:
        continue
print("There were", count, "lines in the file with From as the first word")
