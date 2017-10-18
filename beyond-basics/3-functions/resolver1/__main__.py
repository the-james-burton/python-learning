print('hello...')

from resolver1 import resolver
import timeit

def resolve_timed(func, param):
    start_time = timeit.default_timer()
    func(param)
    time = timeit.default_timer() - start_time
    print("{:f}".format(time))


resolve = resolver.Resolver()
resolve_timed(resolve, 'python.org')
resolve_timed(resolve, 'python.org')

print(resolve._cache)