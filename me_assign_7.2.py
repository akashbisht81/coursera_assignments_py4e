# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count=0.0
sum=0.0
fh = open(fname)
for line in fh:
    line=line.strip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    atpos=line.find(':')
    ppos=line[atpos+1:]
    sum=float(sum)+float(ppos)
    print(line)

print("Done")
avg=sum/count
print(float(avg))
