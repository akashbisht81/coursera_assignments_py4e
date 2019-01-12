
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
dic=dict()
for line in fhand:
    if line.startswith('From '):
        word=line.split()
        # print(word)
        words=word[1]
        # print(words)
        # for i in words:
        dic[words]=dic.get(words,0)+1
# print(dic)
bigcount=None
bigword=None
for big in dic:
    value=dic[big]
    if bigcount==None or value > bigcount:
        bigword=big
        bigcount=value


print(bigword,bigcount)
