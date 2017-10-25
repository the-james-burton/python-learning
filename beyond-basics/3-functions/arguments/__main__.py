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

arguments.print_args("hello", foo="woo", bar="yay")
print(arguments.tag("a", href='/images/test.jpg', style='margin-top:1px'))