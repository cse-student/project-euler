import time

def solution(n):
    largest_digit = resolve_largest_num(n)
    palindrome_list = build_palindrome_list(n, largest_digit)
    for palindrome in palindrome_list:
        for i in range(largest_digit, 0, -1):
            dividend  = palindrome / i
            if (len(str(int(dividend))) > n):
                break
            if ((int(dividend) == dividend) and len(str(int((dividend)))) == n):
                return palindrome        

def resolve_largest_num(n):
    largest_digit = ""
    for _ in range(n):
        largest_digit = largest_digit + "9"
    return int(largest_digit)

def build_palindrome_list(max_digit, largest_num):
    largest_product = largest_num**2
    largest_product_str = str(largest_product)
    first_half  = largest_product_str[0:int(len(largest_product_str)/2)]
    mid_number = ""
    if (largest_product % 2 == 0):
        mid_number = largest_product_str[int(len(largest_product_str)/2):int(len(largest_product_str)/2)+1]
    result = []
    for i in range(int(first_half), 0, -1):
        palindrome = int(str(i) + mid_number + str(i)[::-1])
        result.append(palindrome)
    return result


start = time.time()
print(solution(3))
end = time.time()
print(end - start)

