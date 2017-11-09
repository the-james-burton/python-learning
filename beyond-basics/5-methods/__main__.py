print('methods...')

from shipping import *


c1 = ShippingContainer('ABC', 20, 'Toys')
print(c1)

c2 = ShippingContainer('DEF', 10, 'Umbrellas')
print(c2)

c3 = ShippingContainer.create_empty('GHI', 20)
print(c3)

c4 = ShippingContainer.create_with_items('JKL', 20, ['Dogs', 'Cats', 'Rain'])
print(c4)

rc1 = RefrigeratedShippingContainer('JKL', 20, 'Meat', celsius=2.8)
print(rc1)

rc2 = RefrigeratedShippingContainer('JKL', 20, 'Ice Cubes', celsius=1.2)
print(rc2)

rc3 = RefrigeratedShippingContainer.create_empty('JKL', 20, celsius=2.5)
print(rc3)

rc4 = RefrigeratedShippingContainer.create_with_items('JKL', 20, ['Butter', 'Cheese', 'Cream'], celsius=1.5)
print(rc4)

try:
    rc4.celsius = 5.0
except ValueError as e:
    print(e)

rc4.celsius = 1.0
print(rc4.fahrenheit)
rc4.fahrenheit = 32.5
print(rc4.celsius)


hrc1 = HeatedRefrigeratedShippingContainer('JKL', 20, 'Meat', celsius=2.8)
print(hrc1)

try:
    hrc1.celsius = -30.0
except ValueError as e:
    print(e)

try:
    hrc1.celsius = 15.0
except ValueError as e:
    print(e)


try:
    # this works because the fahrenheit setter
    # delegates to the celsius property setter...
    hrc1.fahrenheit = -55.0
except ValueError as e:
    print(e)
