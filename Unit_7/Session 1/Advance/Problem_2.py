def reverse_orders(orders: str) -> str:
    words = orders.split(" ")
    
    def helper(i: int) -> list[str]:
        if i < 0:
            return []
        return [words[i]] + helper(i - 1)
    
    return " ".join(helper(len(words) - 1))


print(reverse_orders("Bagel Sandwich Coffee"))
