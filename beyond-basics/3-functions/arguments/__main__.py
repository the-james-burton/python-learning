print('functions...')

from pprint import pprint
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

# the trace() function wraps the call to the int() constructor...
arguments.trace(int, "ff", base=16)

jan = [1,2,3]
feb = [4,5,6]
mar = [7,8,9]

for i in zip(jan, feb, mar):
    print(i)

# list of lists...
months = [jan, feb, mar]

# without argument unpacking...
for i in zip(months[0], months[1], months[2]):
    print(i)

# with argument unpacking...
transposed = list(zip(*months))
pprint(transposed)
