def solution(n):
    squareOfSum = (((n+1)*n)/2)**2
    sumOfSquare = (n*(n+1)*((2*n)+1))/6
    return int(squareOfSum - sumOfSquare)

print(solution(100))