# The sieve of Eratosthenes is one of the most efficient
# ways to find all primes smaller than n when n is smaller
# than 10 million or so

def sieve(n):
    prime = [0 for i in range(1011)]
    for i in range(2, n+1):
        prime[i] == 0
        for j in range(i*i, n+1, i):
            prime[j] = 1
    for i in range(2, n+1):
        if prime[i] == 0:
            print(i, end=" ")
sieve(500)