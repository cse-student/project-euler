def solution(n):
    max1 = int((n-1) / 3)
    max2 = int((n-1) / 5)
    lst1 = [i for i in (3*j for j in range(1,max1+1))]
    lst2 = [i for i in (5*j for j in range(1,max2+1))]
    return sum(set(lst1+lst2))

print(solution(1000))