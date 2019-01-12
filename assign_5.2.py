largest = -1;
smallest = None
while True:

        inp = input("Enter a number: ")
        if inp == "done" : break
        try:
            num=int(inp)
        except:
            print("Invalid input")
            continue
        #print(num)
        if int(largest)<int(num):
            largest=num
        if smallest is None or num<smallest:
            smallest=num
print("Maximum is", largest)
print("Minimum is",smallest)
