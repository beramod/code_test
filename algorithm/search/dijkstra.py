import heapq
from . import Search

class Dijkstra(Search):
    def search(self, graph, start):
        visit = {start: 0}
        queue = []
        heapq.heappush(queue, (0, start))
        
        while queue:
            dis, node = heapq.heappop(queue)
            
            if visit.get(node) != None and (visit.get(node) < dis):
                continue
            
            for new_node, new_dis in graph.get(node).items():
                if not visit.get(new_node) == None or (visit.get(new_node) > new_dis + dis):
                    visit[new_node] = new_dis + dis
                    heapq.heappush(queue, (new_dis + dis, new_node))
        return visit