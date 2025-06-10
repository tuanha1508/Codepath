def final_value_after_operations(operations):
    res = 1
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            res += 1
        else:
            res -= 1
    print(res)

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)