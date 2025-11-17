from collections import deque
from heapq import *

graph = {
    0: [(1,3), (4,5), (2,1), (6,9)],
    1: [(7,1), (5,6), (4,3)],
    2: [(3,3), (2,2)],
    3: [],
    4: [(8,8)],
    5: [],
    6: [],
    7: [(6,5)],
    8: [(4,8)],
    9: [(8,6)]
}

distances = {}
pq = []
heappush(pq, (0,0))
while len(pq) > 0:
    distance,node = heappop(pq)
    if node not in distances.keys():
        distances[node] = distance
        for child, weight in graph[node]:
            if child not in distances.keys():
                heappush(pq,(distance+weight, child))
print(distances)