print('lambda...')

people = ['Dawn White',
          'Andrew Zulu',
          'Brian Yellow',
          'Emily Van',
          'Charlie Xavier'
          ]


people_sorted = sorted(people, key=lambda name: name.split()[-1])

print(people_sorted)