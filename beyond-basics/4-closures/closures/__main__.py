print('closures...')

from closures.closure import raise_to
from closures.enclosing import enclosing, get_message

square = raise_to(2)
cube = raise_to(3)

print(square.__closure__)
print(cube.__closure__)

print(square(3))
print(cube(3))


print('global message:', get_message())
enclosing()
print('global message:', get_message())
