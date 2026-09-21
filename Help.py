s = input()
mx_s = s
mn_s = s

while s != 'КОНЕЦ':
    if s < mn_s:
        mn_s = s
    if s > mx_s:
        mx_s = s

    s = input()

print(f'Минимальная строка ⬇️: {mn_s}')
print(f'Максимальная строка ⬆️: {mx_s}')