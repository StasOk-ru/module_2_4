# Задача "Всё не так уж просто":

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #, 16, 17, 18, 19, 20]
primes = []
not_primes = []
print('в списке', len(numbers), 'элементов')
for i in range(len(numbers)):
    is_prime = 0
    if numbers[i] == 1:
        print(f'число 1 не простое, и не сложное, не учитываем')
        continue

    for j in numbers:
        b = numbers[i] % j

        if b == 0 and 1 < j < numbers[i]:
            is_prime = 1
            break

    if is_prime == 1:
        #print(f'число {numbers[i]} сложное')  # сложное
        not_primes.append(numbers[i])
    if is_prime == 0:
        primes.append(numbers[i])

print('Простые: ',primes)
print('Сложные: ', not_primes)
