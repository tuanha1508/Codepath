def longest_substring(s, k):
    if len(s) < k:
        return 0
    
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i, char in enumerate(s):
        if freq[char] < k:
            left = longest_substring(s[:i], k)
            right = longest_substring(s[i+1:], k)
            return max(left, right)

    return len(s) 

print(longest_substring("tatooine", 2))
print(longest_substring("chewbacca", 2))
