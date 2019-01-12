score=input("Enter Score")

try:
    s=float(score)
    if 0.0<=s<=1.0:
        if s>=0.9:
            print('A')
        elif s>=0.8:
            print('B')
        elif s>=0.7:
            print('C')
        elif s>=0.6:
            print('D')
        elif s<0.6:
            print('F')
    else:
        print('out of scope')
except:
    print('Bad score')
#internet history and security
