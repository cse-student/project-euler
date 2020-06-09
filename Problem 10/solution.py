def solution(n):
    result = 0
    for i in range(2, n):
        if (isPrime(i)):
            result += i
    return result

def isPrime(n):
    max = int(n**(1/2))
    for i in range(2,max+1):
        if n % i == 0:
            return False
    return True

print(solution(2000000))