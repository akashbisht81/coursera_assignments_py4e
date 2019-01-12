def computepay(hrs,rate):
	h=float(hrs)
	r=int(rate)
	if h>40:
	    cal=h-40
	    apay=cal*r*1.5
	    pay=(h-cal)*r
	    fpay=pay+apay
		return fpay
		#print(fpay)
	else:
	    pay=h*r
	    print("",pay)


hrs=input('Enter the Hours value')
rate=input('Enter the Rate value')
res=computepay(hrs,rate)
print(res)
