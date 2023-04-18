def sieve_of_eratosthenes(n):
    """Находит все простые числа от 2 до n."""
    # Создаем список чисел от 2 до n.
    numbers = list(range(2, n+1))
    primes = []

    while numbers:
        # Берем первое число из списка, оно обязательно простое.
        prime = numbers.pop(0)
        primes.append(prime)

        # Удаляем все кратные ему числа из списка.
        for num in numbers:
            if num % prime == 0:
                numbers.remove(num)

    return primes

n = int(input("Введите верхнюю границу диапазона: "))
primes = sieve_of_eratosthenes(n)
print("Простые числа в диапазоне от 2 до", n, ":", primes)
