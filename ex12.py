arr = []
sum=0
n=5  
flag=0
input_str = input("Enter array elements separated by spaces: ")

elements = input_str.split()


for element in elements:
    arr.append(int(element))

print("Array elements:", arr)
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]==0:
                flag=1
                break
            
        if flag==1:
            break
    if flag==1:
        break

if(flag==1):
    print("1")
else:
    print("0")   



# arr = []
# sum=0
# n=5  
# flag=0
# input_str = input("Enter array elements separated by spaces: ")

# elements = input_str.split()


# for element in elements:
#     arr.append(int(element))

# print("Array elements:", arr)
# for i in range(0,n):
#     for j in range(0,n):
#         for k in range(0,n):
#             if(arr[i]+arr[j]+arr[k]==0):
#                 flag=1
# if(flag==1):
#     print("1")
# else:
#     print("0")
