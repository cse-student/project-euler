def solution(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if (a + b + c == n and a**2 + b**2 == c**2):
                    print("a", a)
                    print("b", b)
                    print("c", c)
                    return a*b*c
                    
print(solution(1000))