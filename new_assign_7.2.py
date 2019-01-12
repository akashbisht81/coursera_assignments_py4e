# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for each in fh:
    ly=each.rstrip()
    UC=ly.upper()
    print(UC)
