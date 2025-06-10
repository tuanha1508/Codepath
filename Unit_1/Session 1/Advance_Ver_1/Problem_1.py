def linear_search(lst, target):
    if target in lst:
        print(lst.index(target))
    else :
        print(-1)
    pass

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)
