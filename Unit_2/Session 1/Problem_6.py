def organize_pirate_crew(group_sizes):
    size_to_pirates = {}
    for pirate_id, size in enumerate(group_sizes):
        if size not in size_to_pirates:
            size_to_pirates[size] = []
        size_to_pirates[size].append(pirate_id)
    
    result = []
    
    for size, pirates in size_to_pirates.items():
        for i in range(0, len(pirates), size):
            group = pirates[i:i+size]
            result.append(group)
    
    return result

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2))