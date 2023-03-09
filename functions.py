# print('hello')

# str = 'Hello from python'
# print(str)
# mystr = "hello everybody!"
# mylength = len(mystr)
# print(mylength)

# def add(x,y):
#     return x + y
#
# z = add(5, 10)
#
# print(z)
#
# m = 10
# n = 20
# z = add(m,n)
# print(z)
# z = add (10,n)
# print(z)

# m = 'abc'
# n = 'def'
# print(add(m,n))

# def subtract(x,y):
#     return x - y
#
# m = 'abc'
# n = 'def'
# print(subtract(m,n))

# def timestwo(num):
#     return num * 2
# # print(timestwo(5.5))
# # print(timestwo(5))
# # print(type(timestwo(5)))
#
# q = 3.6
# r = timestwo(q)
# print(q)
# print(r)
# print(num)

# def scope(x):
#     return x+1
#
# q = scope(10)
# print(q)
# print(x) #gives error because it is a local variable


# def did_it_change(x):
#     x = 10
#     print('x is now %s while inside the function' % x)
# y = 15
# did_it_change(y)
# print("But back outside the function y is still %s")

# def not_ready(x)
#     pass
#
# not_ready(5.0)
#
# #hypothetically you have code with 3 functions to implement
# def func1():
#     pass
# def func2():
#     pass
# def func3():
#     pass

#first consider regular function like before
def make_pizza(size, stuff_crust = False, cheese_type = 'mozzarella',sauce_type = 'tomato'):
    if stuff_crust:
        print(f'Your {size} inch stuff crust pizza with {cheese_type} cheese and ..')
    else:
        print(f'Your {size} inch pizza with {cheese_type} cheese and {sauce_type}')

make_pizza(14, True, 'mozzarella', 'tomato')
make_pizza(16)
make_pizza(16, True)

#named parameters
def build_info(name, height, number):
    return f'My name is {name}, I am {height} inches tall, and my lucky number is {number}'

result = build_info("Jason", "5-8" ,88)
print(result)

result2 = build_info(name = 'Sally', height = 66, number = 1000)
print(result2)
result3 = build_info(number = 1000,name = 'Sally', height = 66 )
print(result3)

#mixing names and unnamed parameters

