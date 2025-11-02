
# W3 SChools

#list and arrays

x = []

y = [1,2,3,4,5]

z = [1, "hello", 3.14, True]


y.append(8)

print(y)


my_array = [7,12,9,4,11,8]
minVal = my_array[0]

for i in my_array:
    if i<minVal:
        minVal = i

print("minimum value is",minVal)

#stacks

# Stack Implementation using Python Lists

stack = []

stack.append('A')
stack.append('B')
stack.append('C')

print("Stack:", stack)


topEle = stack[-1]
print("peek",topEle)

popedEle = stack.pop()
print(popedEle)

print("stack after pop" ,stack)

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

print("Size", len(stack) )

x.append(8)
x.append(5)
x.append(2)
x.append(90)

print(x)

# x.pop(-1)
# print(x)

# for i in x:
x.sort()
print(x)

print(x[-2])



# x = int(input())
# y = int(input())

# print(x+y)

def get_greeting():
    return "hello from a function"

message = get_greeting()

print(message)

print(get_greeting())


def my_function(fname):
    print(fname + "hello")


my_function("tanishq")


thisset = {"apple", "banana", "cherry"}
print(thisset) 

# thislist = ("apple", "banana", "cherry")
# print(thislist) 

numbers = {10,222,3233,4}
print(numbers)


print(sorted(numbers))


thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" :1964
}

print(thisdict)