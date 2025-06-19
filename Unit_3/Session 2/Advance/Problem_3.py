def max_corridor_area(segments):
    left, right = 0, len(segments) - 1
    max_area = 0

    while left < right:
        height = min(segments[left], segments[right])
        width  = right - left

        max_area = max(max_area, height * width)

        if segments[left] < segments[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == "__main__":
    print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # → 49
    print(max_corridor_area([1, 1]))                      # → 1
