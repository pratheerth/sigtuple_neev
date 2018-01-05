def q_2(nums, target):
    ways = 0
    nums = sorted(nums)
    
    i = len(nums) - 1
    while(i >= 0):
        j = 0
        k = i - 1
        while (j < k):
            if (nums[i] == nums[j] + nums[k]):
                ways += 1
                j += 1
            elif (nums[i] > nums[j] + nums[k]):
                j += 1
            else:
                k -= 1
        i -= 1
        
    return ways

# inputs
length_of_nums = input("How many digits are you testing?: ")
nums = input("Enter the integers: ")
target = len(nums)
#function
print(q_2(nums, target))