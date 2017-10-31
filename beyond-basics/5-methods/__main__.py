print('methods...')

from shipping import *

def print_container(container):
    print("owner={}, contents={}, serial={}".format(
        container.owner, container.contents, container.serial))


c1 = ShippingContainer('ABC', 'Toys')
print_container(c1)

c2 = ShippingContainer('DEF', 'Umbrellas')
print_container(c2)

c3 = ShippingContainer.create_empty('GHI')
print_container(c3)

c4 = ShippingContainer('JKL', ['Dogs', 'Cats', 'Rain'])
print_container(c4)

rc1 = RefrigeratedShippingContainer('JKL', 'Meat')
print_container(rc1)

rc2 = RefrigeratedShippingContainer('JKL', 'Ice Cubes')
print_container(rc2)

