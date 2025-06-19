def build_skyscrapers(floors):
    stack = []
    res = 1
    for i in floors:
        if not stack:
            stack.append(i)
        else:
            if i > stack.pop():
                res += 1
                stack = []
            else :
                stack.append(i)
    
    return res
    pass

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 



