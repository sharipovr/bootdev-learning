def find_min(nums):
    min_so_far = float("inf")
    for num in nums:
        if num < min_so_far:
            min_so_far = num

    return min_so_far