def process_supplies(supplies):
    sorted_supplies = sorted(supplies, key=lambda item: item[1], reverse=True)
    return [name for name, _ in sorted_supplies]
