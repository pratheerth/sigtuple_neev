def q_1(nums):
    nums = [1] + [n for n in nums] + [1]
    dp = [[0]*len(nums) for _ in range(len(nums))]
    for start in range(len(nums) - 2, 0, -1):
        for end in range(start, len(nums) - 1):
            # last balloon
            for k in range(start, end+1):
                dp[start][end] = max(dp[start][end], dp[start][k-1] + dp[k+1][end] + nums[start-1] * nums[k] * nums[end+1])
    return dp[1][len(nums)-2]

test_case = input("Enter the bubble numbers: ")
#test_case = 44, 53, 36, 42, 40, 48, 54, 50, 45, 54, 45, 38, 35, 45, 45, 54, 38

print(q_1(test_case))