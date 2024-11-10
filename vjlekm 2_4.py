# не все так просто
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:  # перебираем элементы
    is_prime = True  # простота числа
    if i == 1:  # кроме равных 1, т.к не входит в условия
        continue
    for j in range(2, i):  # перебираем делители
        if i % j == 0:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime == True:
        primes.append(i)
print(primes)
print(not_primes)
