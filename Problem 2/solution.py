def solution(n):
    lst = []
    i = 1
    x = 1
    while x < n:
        if (x % 2) == 0:
            lst.append(x)
        x = calculate_fibonacci(i)
        i += 1   
    return sum(lst)

def calculate_fibonacci(n):
    if (n < 2):
        return 1
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

# def calculate_fibonacci(n,m):
#     x = (1 + 5**(1/2))/2
#     y = (1 - 5**(1/2))/2
#     z = 5**(1/2)
#     return [i for i in (int((x**j - y**j)/z) for j in range(n))  if i % 2 == 0]

print(solution(4000000))