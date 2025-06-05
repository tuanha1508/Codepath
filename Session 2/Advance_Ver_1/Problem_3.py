def remove_dupes(items):
    if not items:
        print(0)
    res = 1
    for i in range(1, len(items)):
        if(items[i] != items[i - 1]):
            items[res] = items[i]
            res += 1
    print(items)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)