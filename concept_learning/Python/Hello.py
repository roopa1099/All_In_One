print("hello")

var = "Roopa is a girl"
print(var)

print(var.islower())

#right to nleft is negative indexing
print(var[-2])

print(var[0:3])  #slicing
print(var[1:])
print(var[:4])
print(var[0:0])
print(var[0:5])#last index+ 1 index


print(len(var))  #length of string
print(var.title())  #first letter of each word capital

print(var.capitalize())  #first letter of first word capital

type(var)
str = "     -Roopa  is aaa "
print(str.strip())  #removes white spaces in starting and ending
print(var[-4:-2])  #empty string as -2 is greater than -4

print(var.replace("Roopa", "Roooppaaa"))  #replaces Roopa with Roo
var = "Rppaaoa"
print(var.index('o',5))  #gives index of first occurrence of o after index 2

print(var.count('o'))  #counts number of o's in the string

print(var.swapcase())  #swaps the cases


#LIST

list=["hello",3,12.8,True]
print(list)
print(list[0])
print(list[1:3])
print(list[-1])

list.append("Roopa")
print(list)
list.remove(12.8) #removes specific element
print(list)
list.extend(["a","b"]) #adds multiple elements at the end
list.insert(1,"inserted") #inserts at specific index
print(list)
list.pop() #removes last element
print(list)
list.pop(1) #removes element at specific index
print(list)
list.remove("hello") #removes specific element FIRST OCCURRENCE
print(list)
list[0]="newhello" #modifying element at specific index
print(list)
list.count("a") #counts occurrences of specific element
print(list)


for i in list:
    print(i)

newlist=[]
# for i in list:
#     if str(i).islower():
#         newlist.append(i)



# Remove all the occurrences of "apple" from the list
for i in range(list.count("apple")):
    list.remove("apple")


list1 = [1,2,3]
tuple1 = (4,5,6)
set1 = {7,8,9}
# [],(),{} #empty list, tuple, set

# array is not default type in python we have to import it via numpy

set2= {3,1,2,3,4,2}  #sets dont allow duplicates and are unordered(internally unsorted)
# output is sorted
# slicing is not possble in sets
print(set2)

print(tuple1[2])
print(list1[2])

print(len(set2))

disct = {"name":"Roopa", "age":25, "city":"Bangalore"}
print(disct)
print(disct["name"])

for key in disct.keys():
    print(key)  

list1 = [1,2,3,4,5]
tuple1 = (6,7,8,9,10)
dict1= {"list":list1, "tuple":tuple1}

print(dict1["list"][1])  #accessing list element inside dictionary
print(dict1["tuple"][2])  #accessing tuple element inside dictionary

list2 = list1[0:2:1]  #indexing not supported in list slicing

for i in zip(list1, list2):  #zipping two iterables of different lengths, The shortest list wins.
    print(i)



list3 = [3,6,3,1,2,65,768,44,56,76,77,43]

is_even = lambda x:x%2==0

# list comprehension
evenList = [i for i in list3 if is_even(i)]
