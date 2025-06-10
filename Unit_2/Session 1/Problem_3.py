def find_duplicate_chests(chests):
    
    cnt = {}
    
    for i in chests:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    
    duplicates = [chest for chest, count in cnt.items() if count > 1]
    return duplicates
    pass

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))