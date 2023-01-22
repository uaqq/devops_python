n = input('Введите номер билета: ')
odd = 0
even = 0

for i in range(len(n)):
    if i % 2 == 0:
        even += int(n[i])
    else:
        odd += int(n[i])

if even == odd:
    print('Билет счастливый!')
else:
    print('Билет несчастливый!')