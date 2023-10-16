def find_duplicate(nums):
    if len(nums) < 0:
        return False

    nums.sort()
    index = 0
    seen_numbers = set()

    while index < len(nums):
        num = nums[index]
        if not isinstance(num, int) or num < 0:
            return False
        if num in seen_numbers:
            return num
        seen_numbers.add(num)
        index += 1

    return False
