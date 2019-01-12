
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
c = dict()
for line in fhand:
  if not line.startswith('From '): continue
  pieces = line.split()
  print(pieces)
  email = pieces[1]
  c[email] = c.get(email,0) + 1

bigc=None
bige=None
for word in c:
  value=c[word]
  if bigc == None or value > bigc:
    bigw=word
    bigc=value

print(bigw,bigc)
    # words=i.split()
    # if 'From' in words:
        # w=words[1]
        #print(w)
        # sw=w.rstrip()
