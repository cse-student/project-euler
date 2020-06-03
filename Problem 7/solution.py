def solution(n):
    count = 0
    i = 1
    while count != n:
        i += 1
        if (isPrime(i)):
            count += 1
    return i

def isPrime(n):
    max = int(n**(1/2))
    for i in range(2,max+1):
        if n % i == 0:
            return False
    return True
    
print(solution(10001))