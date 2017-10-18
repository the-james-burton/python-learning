print('hello...')

from resolver1 import resolver

resolve = resolver.Resolver()

print(resolve('python.org'))
print(resolve._cache)