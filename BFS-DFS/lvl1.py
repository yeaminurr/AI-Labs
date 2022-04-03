from BFS import bfs
bfs = bfs()
pos = int(input("Enter Positions"))
con = int(input("Enter Connections"))
lunapos = int(input("Luna's Position?"))
startingpos=0
inp = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [2, 3], [3, 5], [3, 6], [4, 8], [4, 7], [5, 6], [6, 7], [7, 8]]

step = bfs.getstep(pos,con,inp,lunapos,0)
print(step)