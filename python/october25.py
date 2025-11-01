print("hello bhai")
print(3+2)
print(4)

x= 5

cu = "tanishq"


print("my age is", x , " and name is", cu)

x =5
x = float(x)
print(type(x))

c,v,b = "hhh", 'deke',"ewiq"

print(c)
print(v)
print(b)

fruits = ["orange", "banana", "cherry"]
x,y,z = fruits

print(x)
print(y)
print(z)

x = "hello"
y = "John"
print(x + y)

b = "tanishq"
print(b[2:5])


a="helloworld"
print(a.upper())

hj = " ahxdjwe. icdsal.  efao.      "
print(hj.strip().upper())

hj = "hello, world"
# print(a.replace("h", "w"))

print(hj.split(","))


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny" ')


b = "Hello, World!"
print(b[4:])

b = "Hello, World!"
print(b[-5:-2])

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is{20*59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# print(10>9)

a = 200
b= 330

if b>a:
    print("yes")
else:
    print("no")

print(bool("Hello"))
print(bool(15))
print(bool(1))

def myFunction():
    return False

if myFunction():
    print("Yes")
else:
    print("No")

x = 200
print(isinstance(x, float))