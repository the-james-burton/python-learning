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

# note how the tuple is unpacked and spread across the arguments...
t = (1,2,3,4,5)
arguments.print_args(*t)

# key names will be mapped onto the argument names in the function...
c = {'blue':34, 'red':12, 'green':23, 'alpha':45}
arguments.colour(**c)

# dict() constructor will create dictionary from kwargs...
d = dict(blue=98, red=87, green=65, alpha=56)
arguments.colour(**d)
