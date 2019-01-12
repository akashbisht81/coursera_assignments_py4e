text = "X-DSPAM-Confidence:    0.8475";
atpos=text.find('0')
#print(atpos)
#extract=text.find('',)
num=text[atpos:]
#conv=float(num)
print(num)
