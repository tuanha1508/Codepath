import heapq
def process_performance_requests(requests):
    queue = []
    for idx, (prior, name) in enumerate(requests):
        queue.append((-prior, idx, name))
        
    heapq.heapify(queue)
    result = []
    while queue:
        _, _, name = heapq.heappop(queue)
        result.append(name)
        
    return result
    pass

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))