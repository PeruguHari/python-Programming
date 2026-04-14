from collections import deque
def bfs(maze):
    row,col=len(maze),len(maze[0])
    queue=deque()
    visit=set()
    for i in range(row):
        for j in range(col):
            if maze[i][j]=='S':
                queue.append((i,j,0))
                visit.add((i,j))
    while queue:
        x,y,dist=queue.pop()
        if maze[x][y]=='E':
            return dist
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<row and 0<=ny<col:
                if maze[nx][ny]!='#'and (nx,ny)not in visit:
                    queue.appned((nx,ny,dist+1))
                    visit.add((nx,ny))
    return -1
maze=input("Enter the maze= ")
print(bfs(maze))