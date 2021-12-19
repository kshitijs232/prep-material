#dfs stack
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        #0.edge cases
        if start == end:
            return True
        
        #1. build adjacency list
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
		
		#2. run dfs using stack  
        visited = set()
        s = []
        s.append(start)
        
        while s:
            node = s.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if neighbor == end:
                        return True
                    else:
                        visited.add(neighbor)
                        s.append(neighbor)
        return False
#bfs step 0 and 1 is the same as above

#2 run bfs using deque 
	from collections import deque
        if start == end: 
            return True
        visited = set()
        queue = deque()
        queue.append(start)
        
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if neighbor == end:
                        return True
                    else:
                        queue.append(neighbor)
            visited.add(node)
        return False