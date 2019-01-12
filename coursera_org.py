

# counts=dict()
# names=['csev','cwen','csev','zqian','cwen']
# for name in names:
    # if name not in counts:
    # counts[name]=1
    # else:
        # counts[name]=counts[name]+1
# print(counts)


# counts=dict()

# names=['zwen','zwen','zwen','zqain','cwex','zwen','zwen','zwen','zqain','cwex','zwen','zwen','zwen','zqain','cwex','zwen','zwen','zwen','zqain','cwex']

# for name in names :
    # counts[name]=counts.get(name, 0) + 1
# print(counts)
#
# for line in counts:
    # print(line,'::',counts[line])


counts=dict()
print('Enter a line/Paragraph of text:')
line=input('')
words=line.split()
#print('words',words)
print('counting')

for word in words:
    counts[word]=counts.get(word,0)+1
#print('Counts',counts)
print('----------------------------------------')
for line in counts:
    print(line,'::',counts[line])
