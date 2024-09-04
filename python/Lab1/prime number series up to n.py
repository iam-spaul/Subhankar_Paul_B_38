n = int(input("Enter the value of n: "))
primes = []
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print(f"Prime numbers up to {n} are: {primes}")
