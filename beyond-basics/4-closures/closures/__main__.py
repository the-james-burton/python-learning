print('closures...')

from closures.closure import raise_to

square = raise_to(2)
cube = raise_to(3)

print(square.__closure__)
print(cube.__closure__)

print(square(3))
print(cube(3))
