def count_layers(sandwich):
    if not sandwich:
        return 0

    first, *rest = sandwich

    if isinstance(first, list):
        first_count = count_layers(first)
    else:
        first_count = 1

    return first_count + count_layers(rest)


sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2)) 
