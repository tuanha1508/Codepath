def is_balanced(code):
    freq = {}
    for char in code:
        freq[char] = freq.get(char, 0) + 1
    
    for letter in freq:
        temp_freq = freq.copy()
        temp_freq[letter] -= 1
        
        if temp_freq[letter] == 0:
            del temp_freq[letter]
        
        if temp_freq:
            frequencies = list(temp_freq.values())
            if all(f == frequencies[0] for f in frequencies):
                return True
    
    return False

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1))
print(is_balanced(code2))