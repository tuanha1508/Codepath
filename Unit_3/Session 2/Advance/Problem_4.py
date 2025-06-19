def min_swaps(s):
    """
    Return the minimum number of swaps of two brackets (anywhere in the string)
    needed to turn s into a balanced layout.
    """
    balance = 0
    min_balance = 0

    for ch in s:
        if ch == '[':
            balance += 1
        else:  # ch == ']'
            balance -= 1
        min_balance = min(min_balance, balance)

    # Each swap fixes 2 units of negative balance:
    return (-min_balance + 1) // 2


if __name__ == "__main__":
    print(min_swaps("][]["))    # → 1
    print(min_swaps("]]][[["))  # → 2
    print(min_swaps("[]"))      # → 0
