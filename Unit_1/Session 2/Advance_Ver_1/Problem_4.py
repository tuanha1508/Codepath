def sort_by_parity(nums):
    left = 0  # Points to position where next even number should go
    right = len(nums) - 1  # Points to position where next odd number should go
    
    while left < right:
        # If left element is even, it's in correct position
        if nums[left] % 2 == 0:
            left += 1
        # If right element is odd, it's in correct position  
        elif nums[right] % 2 == 1:
            right -= 1
        # Left is odd and right is even - swap them
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    print(nums)

nums = [3, 2, 1, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)