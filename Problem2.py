class Solution:
    def countArrangement(self, n: int) -> int:
        count = [0]
        visited = [False for _ in range(n+1)]
        
        def backtrack(start, end, path):
            if len(path) == n:
                count[0] += 1
                return
            
            for i in range(1, n+1):
                if not visited[i]:
                    if i % (len(path)+1) == 0 or (len(path)+1) % i == 0:
                        path.append(i)
                        visited[i] = True
                        backtrack(start + 1, end, path)
                        path.pop()
                        visited[i] = False
        
        backtrack(0, n, [])
        return count[0]