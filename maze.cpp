#include<iostream>
#include<vector>
using namespace std;


bool dfs(vector<vector<int>>& maze, vector<int>& st, vector<int>& dest, int rows, int cols) {
    if (st[0] == dest[0] && st[1] == dest[1])
        return true;
    
    if (st[0] < 0 || st[0] >= maze.size() || st[1] < 0 || st[1] >= maze[0].size() || maze[st[0]][st[1]] == -1)
        return false;
    maze[st[0]][st[1]] = -1;
    vector<vector<int>> dirs = {{0,1},{0,-1},{1,0},{-1,0}};
    for (auto p : dirs) {
        int r = p[0];
        int c = p[1];
        while (c < maze[0].size() && maze[r][c] != -1 && maze[r][c] != 1 && r >= 0 && r < maze.size()) {
            st[0] += r;
            st[1] += c;
            maze[st[0]][st[1]] = -1;
        }
        if (dfs(maze,st,dest,rows,cols))
            return true;  
    }
    return false;
}
bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
    int rows = maze.size();
    int cols = maze[0].size();
    //maze[start[0]][start[1]] = -1;
    return dfs(maze, start, destination, rows,cols);
    
}


int main()
{
    vector<vector<int>> maze = {{0,0,1,0,0},{0,0,0,0,0},{0,0,0,1,0},{1,1,0,1,1},{0,0,0,0,0}};
    vector<int> start = {0,4};
    vector<int> dest = {4,4};
    cout << hasPath(maze,start,dest);

}
