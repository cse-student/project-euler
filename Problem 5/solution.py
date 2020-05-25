def solution(n):
    lst = []
    for i in range(2, n+1):
        lcm = calculate_lcm(i)
        lst.append(lcm)
    result = 1
    for i in range(len(lst)):
        for j in lst[i]:
            result *= j
            for z in range(i+1, len(lst)):
                if (j in lst[z]):
                    lst[z].remove(j)
    return result

def calculate_lcm(n):
    i = 2
    lcm = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n /= i
            lcm.append(int(i))
    if n > 1:
        lcm.append(int(n))
    return lcm

print(solution(20))