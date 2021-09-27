class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int: 
        q = deque([(0,0,0,0)])
        visited = set([0,0,0])
        m_steps = float('inf')
        row = len(grid)
        col = len(grid[0])
        while q:
            x, y, r, steps = q.popleft()
            if x == row - 1 and y == col - 1:
                m_steps = min(steps, m_steps)
            else:
                for i, j in [[-1,0], [1, 0], [0, -1], [0,1]]: #up, down, left, right
                    if 0 <= x + i < row and 0 <= y + j < col:
                        if r < k and (x+i, y+j, r + grid[x+i][y+j]) not in visited:
                            q.append((x+i, y+j, r + grid[x+i][y+j], steps + 1))
                            visited.add((x+i, y+j, r + grid[x+i][y+j]))
                        elif r == k and grid[x+i][y+j] == 0 and (x+i, y+j, r) not in visited:
                            q.append((x+i, y+j, r, steps + 1))
                            visited.add((x+i, y+j, r))
            #print(q)
        return -1 if m_steps == float('inf') else m_steps
        
            
