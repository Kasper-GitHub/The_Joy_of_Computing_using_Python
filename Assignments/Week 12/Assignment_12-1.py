def singleNonDuplicate(nums):
  n = len(nums)
  j = 0
  frequency =  []
  while j < n :
      frequency.append(nums.count(nums[j]))
      j += 1

  distribution = dict(zip(nums, frequency))

  unique_val = [key for (key,value) in distribution.items() if value == 1]

  return unique_val[0]