def next_greatest_letter(letters, target):
    left, right = 0, len(letters) - 1
    result = letters[0]

    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            result = letters[mid]
            right = mid - 1
        else:
            left = mid + 1

    return result

letters = ['a', 'a', 'b', 'c', 'c', 'c', 'e', 'h', 'w']

print(next_greatest_letter(letters, 'a'))
print(next_greatest_letter(letters, 'd'))
print(next_greatest_letter(letters, 'y'))
