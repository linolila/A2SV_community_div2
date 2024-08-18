class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connection_count = {}
        for u, v in edges:
            if u in connection_count:
                connection_count[u] += 1
            else:
                connection_count[u] = 1
            
            if v in connection_count:
                connection_count[v] += 1
            else:
                connection_count[v] = 1
        n = len(edges) + 1  
        for node, count in connection_count.items():
            if count == n - 1:
                return node

        return -1  
