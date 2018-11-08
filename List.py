import random

list_holder = [0,1,2,3]
list_holder.append("new stuff")

print(list_holder[4])

for x in list_holder:
    print()


names = ["hello", "world"]
print(names)
names.append("stuff")
print(names)

for x in names:
    print("name")


# 1.

list_holder1 = [0,1,2,3,4]

print(list_holder1)


# 2.

list_holder2 = [0,1,2,3]
list_holder2[0] = 1
list_holder2[1] = 2
list_holder2[2] = 3
list_holder2[3] = 4
print(list_holder2)


# 3.

list_holder3 = [5,2,9,6,4,8,3,0,7,1,5]
list_holder3.sort()
print(list_holder3)


# 4.

print(max(list_holder3 + list_holder2))


# 5.

list_holder4 = [1,2,3,4]
for x in list_holder4:
    print(x)

# 6.

word = 'abacadabra'
result = ''
for x in range(0, len(word), 2):
    result += word[x]
print(result)


weekdays = ["Sun", "Tues", "Wed", "Thurs", "Fri"]
del weekdays[0]
print(weekdays)

weekdays = ["Sun", "Tues", "Wed", "Thurs", "Fri"]
weekdays.remove("Sun")
print(weekdays)

weekdays.insert(0, "Mon")
print(weekdays)

a = "hello world"
b = "42"
#  c = 42

print(a.isdigit())
print(b.isdigit())
#  print(c.isdigit())


elements = [1, 2, 3, 4, 5]
del elements[2]
print(elements)


rand_list = []
for y in range(0, 6):
    rand_list.append(random.randint(1, 10))
for x in rand_list:
    if x in range(1, 11, 2):
        print("odd", x)
    elif x in range(2, 12, 2):
        print("even", x)


for x in elements:
    print(x)

hello_world = "hello world"
for x in range(len(hello_world)-1, -1, -1):
    print(hello_world[x], end="")


sentence = "you're a wizard harry"
for x in range