import time

def solution(n):
    lst = []
    for i in range(n, 2, -1):
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
    lcm = fetch_from_cache(n)
    if (lcm != None):
        return lcm
    i = 2
    lcm = []
    keys = []
    while i * i <= n:
        temp = fetch_from_cache(n)
        if (temp != None):
            update_cache(keys, list(lcm))
            return lcm + temp
        if n % i:
            i += 1
        else:
            n /= i
            keys.append(int(n))
            lcm.append(int(i))
    if n > 1:
        keys.append(int(n))
        lcm.append(int(n))
    update_cache(keys, list(lcm))
    return lcm

def update_cache(n, lcm):
    if (not caching_enable):
        return
    for i in range(len(n)-1):
        lcm_cache[n[i]] = list(lcm)
        lcm.pop(0)

def fetch_from_cache(n):
    if (not caching_enable):
        return None
    return lcm_cache.get(n)

lcm_cache = {}
caching_enable = True
print(solution(20))