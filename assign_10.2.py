
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic=dict()
for line in handle:
    if line.startswith('From '):
        words=line.split()
        # print(line)
        # for hour in line:
        hour=words[5]

        hr=hour[:2]
        dic[hr]=dic.get(hr,0)+1
        # print(hr)
# print(dic)
lst=list()
for k,v in dic.items():
    new_dic=(k,v)
    lst.append(new_dic)
lst=sorted(lst,reverse=False)

for v,k in lst:
    print(v,k)
        # print(hour)
     # words=line
     # print(words.split())

# print(handle.read())
