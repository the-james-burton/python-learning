print('decorators...')

from decorators.decorate import get_city, get_city2, hello

print(get_city())
print(get_city2())

hello('Mary')
hello('Norma')
hello('Oscar')
hello('Patty')
print(hello.count)