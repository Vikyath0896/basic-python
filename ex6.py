# a="Punith"
# count=0
# for i in a:
#     print(i)
#     count=count+1
# print("the length of string is",count)


#2.Finding word in sentence
# b="Thala for a reason"
 #print("Thala" in b)
#  OR 
# if "Thala" in b:
#     print("Thala is presnt")

# 3.String slicing
# a1="My name is Vikyath"
# print(len(a1))
# print(a1[-8:-1])

# 4.to upper and lowercase
# a="PUNITH"
# b="gowda"
# print(a.lower())
# print(b.upper())


#5.Removing whitespaces
# a="Punith gowda is good boy"
# print(a.strip())

#6.repalcing character
# a="Punith gowda iii"
# print(a.replace("i","e"))

#7.split 
# a="Punith Gowda, is good boy"
# print(a.split(", "))


#8.escaping characters 
# t="My name is \"Punith\"\ wrong output
#       gowda"
# print(t)

#7. conditions 
# a=10
# b=20
# if(b>a):
#     print("b is greater")
# else:
#     print("a is greater")
# print(bool("Hello"))

#8.Operators

#9.Lists
# fruits = {"apple", "orange", "banana"}
# print(fruits)

# for fruit in fruits:
#     print(fruit[1])  # Accessing the second character of each fruit
#inserting
a=["mys","man","bang"]
a.insert(1,"mang")
print(a)
#appending
a.append("mangalore")
print(a)

#extending a list
a=["dosa","chapathi"]
b=["chutney","kurma"]
print(a.extend(b))

#sorting
a=["orange","mango","apple"]
a.sort()
print(a)

b=[55,100,35,69]
# b.sort()
# sorting in descending order
b.sort(reverse=True)
print(b)

#copying
a=[1,2,3,4]
b=a.copy()
print(b)
print(a.extend(b))