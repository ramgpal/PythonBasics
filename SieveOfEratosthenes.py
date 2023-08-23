# The sieve of Eratosthenes is one of the most efficient
# ways to find all primes smaller than n when n is smaller
# than 10 million or so

# def sieve(n):
#     prime = [0 for i in range(1011)]
#     for i in range(2, n+1):
#         prime[i] == 0
#         for j in range(i*i, n+1, i):
#             prime[j] = 1
#     for i in range(2, n+1):
#         if prime[i] == 0:
#             print(i, end=" ")
# sieve(500)

def sieve(n):
    prime = [True for i in range(n+1)]
    prime[0] = prime[1] = False
    i = 2
    while(i*i <= n):
        if (prime[i]):
            for j in range(i*i, n+1, i):
                prime[j] = False
        i += 1
    for i in range(2, n+1):
        if prime[i] == True:
            print(i, end=" ")

sieve(30)
