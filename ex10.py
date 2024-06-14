def myfunction(n):
    if n==0:
        return 0
    else:
        myfunction(n-1)
        print(n)


n=int(input("Enter the number"))
myfunction(n)
# print(m)