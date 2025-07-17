def find_closest_planets(planets, target_distance, k):
    left = 0
    right = len(planets) - k

    while left < right:
        mid = (left + right) // 2
        dist_left = abs(planets[mid] - target_distance)
        dist_right = abs(planets[mid + k] - target_distance)

        if dist_left > dist_right:
            left = mid + 1
        else:
            right = mid

    return planets[left:left + k]

planets1 = [100, 200, 300, 400, 500]
planets2 = [10, 20, 30, 40, 50]

print(find_closest_planets(planets1, 350, 3))
print(find_closest_planets(planets2, 25, 2))
