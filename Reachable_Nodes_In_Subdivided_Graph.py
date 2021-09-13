class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        
        pq = [(0,0)]
        dist = {0:0}
        used = {}
        ans = 0
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            ans += 1
            for neigh, weight in graph[node].items():
                v = min(weight, maxMoves - d)
                used[(node, neigh)] = v
                
                d2 = d + weight + 1
                if d2 < dist.get(neigh, maxMoves+1):
                    heapq.heappush(pq, (d2, neigh))
                    dist[neigh] = d2
        for u, v, w in edges:
            ans += min(w, used.get((u,v), 0)+used.get((v, u), 0))
        return ans
