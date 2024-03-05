a= int((input("How tall (1-8) should the pyramid be? ")))
if a>8 or a<1:
    print ('Enter a number between 1 and 8')
else:
    for i in range(a+1):
        print(" "*(a-i)+'#'*i)
    print()