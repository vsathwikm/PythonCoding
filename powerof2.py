# Simple program to find out if a number (integer or decimal) is a power of 2 or not
x = [4,64,-5,65,0.25,0.5,1]
for i in x:
    num = float(i)
    if num>1:
        if num%2 == 1:
            print ("0\n")
        else:
            while num>2 and num%2 == 0:
                num = num/2
                rem = num%2
            if rem == 0:
                print ("1\n")
            else:
                print ("0\n")
    elif num == 1:
        print ("1\n")
    else:
        while num<1 and num>0:
            num = num*2
        if num == 1:
            print ("1\n")
        else:
            print ("0\n")
