print('decorators...')

from pprint import pprint
from decorators.decorate import get_city, get_city2, hello, tracer, rotate_list, norge_it

print(get_city())
print(get_city2())

hello('Mary')
hello('Norma')
hello('Oscar')
hello('Patty')
print(hello.count)

numbers = [1,2,3]
pprint(numbers)
numbers = rotate_list(numbers)
pprint(numbers)
tracer.enabled = False
numbers = rotate_list(numbers)
pprint(numbers)

print(norge_it("Turtle"))