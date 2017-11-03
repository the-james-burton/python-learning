print('methods...')

from shipping import *

def print_container(container):
    # volume is a property, although this is not directly visible here...
    print("owner={}, length={}, volume={}, contents={}, serial={}".format(
        container.owner, container.length, container.volume, container.contents, container.serial))


c1 = ShippingContainer('ABC', 20, 'Toys')
print_container(c1)

c2 = ShippingContainer('DEF', 10, 'Umbrellas')
print_container(c2)

c3 = ShippingContainer.create_empty('GHI', 20)
print_container(c3)

c4 = ShippingContainer.create_with_items('JKL', 20, ['Dogs', 'Cats', 'Rain'])
print_container(c4)

rc1 = RefrigeratedShippingContainer('JKL', 20, 'Meat', celsius=2.8)
print_container(rc1)

rc2 = RefrigeratedShippingContainer('JKL', 20, 'Ice Cubes', celsius=1.2)
print_container(rc2)

rc3 = RefrigeratedShippingContainer.create_empty('JKL', 20, celsius=2.5)
print_container(rc3)

rc4 = RefrigeratedShippingContainer.create_with_items('JKL', 20, ['Butter', 'Cheese', 'Cream'], celsius=1.5)
print_container(rc4)

try:
    rc4.celsius = 5.0
except ValueError as e:
    print(e)

rc4.celsius = 1.0
print(rc4.fahrenheit)
rc4.fahrenheit = 32.5
print(rc4.celsius)


hrc1 = HeatedRefrigeratedShippingContainer('JKL', 20, 'Meat', celsius=2.8)
print_container(hrc1)

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
