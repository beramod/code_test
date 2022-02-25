from . import Search

class DFS(Search):
    def search(self, graph, start):
        stack = list([start])
        visited = [] * len(graph)
        
        while stack:
            n = stack.pop()
            if n not in visited:
                visited.append(n)
                for m in graph[n]:
                    stack.append(m)
        return visited