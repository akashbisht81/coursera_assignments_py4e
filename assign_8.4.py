# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
    # new=line.rstrip().split()
    #print(new)
    # for i in new:
        # if i in lst:
            # continue
        # else:
            # lst.append(i)
# lst.sort()
# print(lst)




fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    aas=line.rstrip()
    nwk=aas.split()
    # print(nwk)

    for i in nwk:
        if i in lst:
            continue
        else:
            lst.append(i)
lst.sort()
print(lst)
    #new_list=stripped.split()

#print(new_list)
