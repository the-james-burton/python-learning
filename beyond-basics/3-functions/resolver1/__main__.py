print('hello...')

from resolver1 import resolver
import timeit

def resolve_timed(func, param):
    start_time = timeit.default_timer()
    func(param)
    time = timeit.default_timer() - start_time
    print("{:f}".format(time))


resolve = resolver.Resolver()
print(resolve.has('python.org'))
resolve_timed(resolve, 'python.org')
resolve_timed(resolve, 'python.org')
print(resolve.has('python.org'))

print(resolve._cache)
resolve.clear()
print(resolve._cache)
print(resolve.has('python.org'))
resolve_timed(resolve, 'python.org')
resolve_timed(resolve, 'python.org')
print(resolve.has('python.org'))
