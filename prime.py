#wrong                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

n = int(input("Enter  the number:"))
c=0
for i in range(1,n+1):
    if(n%i == 0):
        print(i)
        c = c + 1
if(c == 2):
    print("prim number")
else:
    print("not prim number")