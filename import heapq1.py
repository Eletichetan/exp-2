import heapq

def astar_water_jug():
    capX, capY, target = 7, 4, 6
    start = (0, 0)

    # heuristic: distance from target in container X
    h = lambda s: abs(s[0] - target)

    pq = [(h(start), 0, start, [])]
    visited = set()

    while pq:
        _, g, (x, y), path = heapq.heappop(pq)

        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]

        # goal test
        if x == target:
            return path

        # possible actions
        next_states = {
            (capX, y),                      # fill X
            (x, capY),                      # fill Y
            (0, y),                         # empty X
            (x, 0),                         # empty Y
            (x - min(x, capY - y), y + min(x, capY - y)),  # X → Y
            (x + min(y, capX - x), y - min(y, capX - x))   # Y → X
        }

        for n in next_states:
            heapq.heappush(pq, (g + 1 + h(n), g + 1, n, path))

    return None
