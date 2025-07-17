def find_frequency_positions(transmissions, target_code):
    def find_first():
        left, right = 0, len(transmissions) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if transmissions[mid] == target_code:
                result = mid
                right = mid - 1
            elif transmissions[mid] < target_code:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def find_last():
        left, right = 0, len(transmissions) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if transmissions[mid] == target_code:
                result = mid
                left = mid + 1
            elif transmissions[mid] < target_code:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first = find_first()
    last = find_last()

    return (first, last) if first != -1 else (-1, -1)

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))
