def season(m):
    if m == 12 or  m == 1 or m == 2:
        return 'zima'
    if m > 2 and m < 6:
        return 'vesna'
    if m > 5 and m < 9:
        return 'leto'
    if m > 8 and m < 12:
        return 'osen'
print(season(int(input('Введите номер месяца: '))))
