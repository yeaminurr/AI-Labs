from BFS import bfs
bfs1 = bfs()
#bfs2=bfs()
pos = int(input("Enter Positions"))
con = int(input("Enter Connections"))
inp = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [2, 3], [3, 5],  [4, 8], [4, 7], [5, 6], [6, 7], [7, 8]]
lastpos=int(input("Lina's Position?"))
nora=int(input("Nora's Position?"))

lara=int(input("Lara's Position?"))
larastep = bfs1.getstep(pos,con,inp,lastpos,lara)
norastep = bfs1.getstep(pos,con,inp,lastpos,nora)
larastep = bfs1.getstep(pos,con,inp,lastpos,lara)
if(larastep>norastep):
    print("Nora winner")
elif(norastep>larastep):
    print("Lara winner")
else:
    print("Both won")