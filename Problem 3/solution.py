def solution(n):
    i = 2
    max = 0
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n /= i
            max = i
    if n > 1:
        if (n > max):
            max = n
    return max

print(solution(600851475143))