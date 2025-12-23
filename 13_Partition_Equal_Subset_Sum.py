def can_partition(nums):
    total_sum = sum(nums)
    # If the total sum is odd, we cannot split it into two equal integers
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    # dp[i] will be true if sum 'i' can be reached
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
            
    return dp[target]

print(f"Can partition: {can_partition([1, 5, 11, 5])}") # True: {1, 5, 5} and {11}