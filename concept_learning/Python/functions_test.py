#basic sytax

def add(a, b):
    return a + b

print(add(3, 5))

def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

print(calculate_area(5))


#lambda function
add1 = lambda a,b : a+b

print(add1(3, 5))

isEven = lambda x : x%2 ==0

print(isEven(4))    

str = ["apple", "banana", "cherry"]

listOut = list(map(lambda x : x.upper(),str))

print(listOut)

num = [1,2,3,4,5,6,7,8,9,10]
listEeven = list(filter(lambda x : x%2==0,num)) #filter or name only will return the addreess where output is saved
print(listEeven)


