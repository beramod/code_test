from collections import deque
from . import Search

class BFS(Search):
    def search(self, graph, start):
        que = deque([start])
        visited = [] * len(graph)
        
        while que:
            n = que.popleft()
            if n not in visited:
                visited.append(n)
                for m in graph[n]:
                    que.append(m)
        return visited