print('functions...')


import arguments

print(arguments.hypervolume(2))
print(arguments.hypervolume(2, 2))
print(arguments.hypervolume(2, 2, 2))
try:
    print(arguments.hypervolume())
except BaseException as e:
    print(type(e))

print(arguments.hypervolume2(2))
print(arguments.hypervolume2(2, 2))
print(arguments.hypervolume2(2, 2, 2))

try:
    print(arguments.hypervolume2())
except TypeError as e:
    print(e)

arguments.print_kwargs("hello", foo="woo", bar="yay")
print(arguments.tag("a", href='/images/test.jpg', style='margin-top:1px'))

t = (1,2,3,4,5)
# note how the tuple is unpacked and spread across the arguments...
arguments.print_args(*t)