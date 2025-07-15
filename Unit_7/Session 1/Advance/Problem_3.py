def can_split_coffee(coffee, n):
    
    total = sum(coffee)
    if total % n:
        return False
    target = total // n

    coffee.sort(reverse=True)
    if coffee[0] > target:
        return False

    buckets = [0] * n
    
    def assign(i):
        if i == len(coffee):
            return True

        v = coffee[i]
        
        def try_bucket(j):
            if j == n:
                return False 
            
            if buckets[j] + v <= target:
                
                buckets[j] += v
                
                if assign(i + 1):
                    return True
                
                buckets[j] -= v
                
            if buckets[j] == 0:
                return False
            
            return try_bucket(j + 1)

        return try_bucket(0)

    return assign(0)


print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
