def checkSubsequenceSum(nums, k):
    possible_sums = set([0])  # Start with just the empty subsequence sum

    for num in nums:
        new_sums = set()
        for s in possible_sums:
            new_sums.add(s + num)  # Include current num in the sum
        possible_sums.update(new_sums)  # Merge with previous sums

    return k in possible_sums