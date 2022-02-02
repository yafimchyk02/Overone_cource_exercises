N = 10
A = [0]*N
print('Введите 10 значений массива:')
for i in range(N):
    A[i] = int(input())
print(A)
a = int(input('Введите ещё одно значение'))
b = int(input('Выберите позицию в массиве'))
A.insert(b-1,a)
print(A)