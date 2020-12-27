primes = []

for i in range(1, 101):
    if i == 1:
        continue
    for p in range(2, i):
        if i % p == 0:
            break
    else:
        primes.append(i)

for k in range(1, i+1):
    if k % 3 == 0 and k % 5 == 0 and k in primes:
        print(f"{k}: Prime, FizzBuzz")
    elif k % 3 == 0 and k % 5 == 0:
        print(f"{k}: FizzBuzz")
    elif k % 3 == 0 and k in primes:
        print(f"{k}: Prime, Fizz")
    elif k % 3 == 0:
        print(f"{k}: Fizz")
    elif k % 5 == 0 and k in primes:
        print(f"{k}: Prime, Buzz")
    elif k % 5 == 0:
        print(f"{k}: Buzz")
    elif k in primes:
        print(f"{k}: Prime")
    else:
        print(k)
