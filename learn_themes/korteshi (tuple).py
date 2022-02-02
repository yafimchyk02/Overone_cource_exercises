import random
from statistics import mean
a = [random.randint(0,9) for i in range(9)]
print(a,'sum: ',sum(a))

b = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и',
	         'и', 'и', 'т', 'т', 'а', 'и', 'и',
	         'и', 'и', 'и', 'т', 'и')
print('т:',b.count('т'))
print('и:',b.count('и'))
print('а:',b.count('а'))

week_temp = (26, 29, 34, 32, 28, 26, 23)
print('Средняя темепратура: ',mean(week_temp))


