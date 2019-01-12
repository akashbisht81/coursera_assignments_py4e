
def computepay(hrs,rate):
#hrs=input("Enter Hours:")
    h=float(hrs)
#rate=input("Enter rate")
    r=float(rate)
    if h>40:
        cal=h-40
        apay=cal*r*1.5
        pay=(h-cal)*r
        fpay=pay+apay
        return fpay
        #print(fpay)
    else:
        pay=h*r
        return pay
        #print("",pay)


hrs=input('Enter the Hours')
rate=input('Enter the rate')
res=computepay(hrs,rate)
print(res)
