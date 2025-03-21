def findMaxConsecutiveOnes(nums):
    streak_counter = 0
    strong_signals = []
    for i in range(1,len(nums)):
        if nums[i] == 1:
            if streak_counter == 0: streak_counter = 1
        if nums[i] == nums[i - 1] and nums[i] == 1:
            streak_counter += 1
        else:
            strong_signals.append(streak_counter)
            streak_counter = 0
        strong_signals.append(streak_counter)
    return max(strong_signals)

nums = eval(input())
print(findMaxConsecutiveOnes(nums),end='')