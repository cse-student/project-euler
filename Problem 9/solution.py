def solution(n):
    for a in range(1, n):
        for b in range(1, n):
            d = a**2 + b**2
            c = d**(1/2)
            if (a + b == n - c):
                return int(a*b*c)

print(solution(1000))