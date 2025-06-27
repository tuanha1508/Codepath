def find_best_fabric_pair(fabrics, budget):
    sorted_f = sorted(fabrics, key=lambda x: x[1])
    left, right = 0, len(sorted_f) - 1

    best_sum = -1
    best_pair = (None, None)

    while left < right:
        cost_sum = sorted_f[left][1] + sorted_f[right][1]
        if cost_sum > budget:
            right -= 1
        else:
            if cost_sum > best_sum:
                best_sum = cost_sum
                best_pair = (sorted_f[left][0], sorted_f[right][0])
            left += 1

    return best_pair

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))