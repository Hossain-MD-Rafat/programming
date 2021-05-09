def sumBase(n: int, k: int) -> int:
    nums = []
    sum = 0
    while n>=k:
        nums.append(n % k)
        n //= k
    nums.append(n)
    for x in nums:
        print(x)
        sum += x
    return sum
print(sumBase(10, 10))
