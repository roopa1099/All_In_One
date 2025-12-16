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
for i in list:
    if str(i).islower():
        newlist.append(i)



# Remove all the occurrences of "apple" from the list
for i in range(list.count("apple")):
    list.remove("apple")