def missingNumber(nums):
    for i in range(len(nums)+1):
      try:
        index_pos = nums.index(i)
      except ValueError:
        return i