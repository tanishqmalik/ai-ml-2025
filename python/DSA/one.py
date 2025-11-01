
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

