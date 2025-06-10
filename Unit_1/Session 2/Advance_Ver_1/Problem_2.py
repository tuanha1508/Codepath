def reverse_list(lst):
    # Initialize two pointers
    left = 0               
    right = len(lst) - 1   
    
    # Continue until pointers meet in the middle
    while left < right:
        # Swap elements at left and right positions
        lst[left], lst[right] = lst[right], lst[left]
        
        # Move pointers towards each other
        left += 1  
        right -= 1  

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)
print(lst)