import heapq
def trapRainWater(heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        R = len(heightMap)
        if R == 0:
            return 0
        C = len(heightMap[0])
        
        hq = []
        heapq.heapify(hq)
        seen = set()
        
        for r in range(R):
            for c in range(C):
                if r==0 or c==0 or r==R-1 or c==C-1:
                    heapq.heappush(hq,(heightMap[r][c],r,c))
                    seen.add((r,c))
        
        res = 0
        while hq:
            h,r,c = heapq.heappop(hq)
            nxt_points = {(r+1,c),(r-1,c),(r,c-1),(r,c+1)}
            
            for nxt_r,nxt_c in nxt_points:
                if 0<=nxt_r<R and 0<=nxt_c<C and (nxt_r,nxt_c) not in seen:
                    res += max(0,h-heightMap[nxt_r][nxt_c])
                    heapq.heappush(hq,(max(h,heightMap[nxt_r][nxt_c]),nxt_r,nxt_c))
                    seen.add((nxt_r,nxt_c))
        
        return res

heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print trapRainWater(heightMap)
