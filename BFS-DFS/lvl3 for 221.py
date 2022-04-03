from BFS import bfs
bfs1 = bfs()
pos = int(input("Enter Positions"))
con = int(input("Enter Connections"))
inp = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [2, 3], [3, 5],[4,7],  [4, 8], [4, 7], [5, 6], [6, 7],[6,9], [7, 8],[8,9]]
revinp = list()
for i in inp:
    rev = i[::-1]
    revinp.append(rev)
#print(revinp)

lastpos=int(input("Lina's Position?"))
par = int(input("Number of participants "))
val = bfs1.getstep(pos,con,revinp,0,lastpos)
visited= bfs1.visited
#print(visited)
dic = dict()
minmove=pos
for i in range(par):
    val = int(input(f"For {i}"))
    if val in visited:
        z= visited.index(val)
        #print(z)
        if z<minmove:
            minmove = z
            #print(minmove)

print(minmove)