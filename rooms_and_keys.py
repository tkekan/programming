from collections import defaultdict
class Solution(object):
    def dfs(self, index, visited, rooms, dic):
        visited[index] = True
        for items in rooms[index]:
            dic[items] = True
            if visited[items] == False and dic.get(index, False):
                self.dfs(items, visited, rooms, dic)
            
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        dic = dict()
        if len(rooms):
            dic[0] = True
            for index in range(0, len(rooms)):
                if visited[index] == False and dic.get(index, False) == True:
                    self.dfs(index,visited, rooms, dic)

        return reduce(lambda x, y: x * y, visited)

s = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print s.canVisitAllRooms(rooms)
