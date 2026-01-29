import heapq

def astar_fuel(target):
    capA, capB = 7, 10
    start = (0, 0)

    # heuristic: distance from target
    h = lambda s: min(abs(s[0] - target), abs(s[1] - target))

    pq = [(h(start), 0, start, [])]
    visited = set()

    while pq:
        _, g, (a, b), path = heapq.heappop(pq)

        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]

        # goal check
        if a == target or b == target:
            return path

        # possible operations
        next_states = {
            (capA, b),                         # fill A
            (a, capB),                         # fill B
            (0, b),                            # empty A
            (a, 0),                            # empty B
            (a - min(a, capB - b), b + min(a, capB - b)),  # A → B
            (a + min(b, capA - a), b - min(b, capA - a))   # B → A
        }

        for n in next_states:
            heapq.heappush(pq, (g + 1 + h(n), g + 1, n, path))

    return None
