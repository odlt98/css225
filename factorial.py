a = int(input ("Please enter non negative number. "))
if a is 0:
    print ("1")
else:
    f = 1
    for x in range(1,a):
        f=f*x
    print (f)
