from BFS import bfs
bfs1 = bfs()
#bfs2=bfs()
pos = int(input("Enter Positions"))
con = int(input("Enter Connections"))
inp = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [2, 3], [3, 5],[4,7],  [4, 8], [4, 7], [5, 6], [6, 7],[6,9], [7, 8],[8,9]]
lastpos=int(input("Lina's Position?"))
par = int(input("Number of participants "))
# file= open("input3.txt.txt")
# inp = list()
# participant = list()
# count = 0
# for i in file:
#     i = i.rstrip()
#     if count==0:
#         pos = int(i)
#     elif count == 1 :
#         con = int(i)
#     elif count==con+2:
#         lastpos = int(i)
#     elif count==con+3:
#         par = int(i)
#         for j in range(par):
#             value = file.readline()
#             value = int(value)
#             value = bfs1.getstep(pos,con,inp,lastpos,value)
#             participant.append(value)
#
#
#     else:
#         inp1 = i.split(" ")
#         inp1[0]= int(inp1[0])
#         inp1[1] = int(inp1[1])
#         inp.append(inp1)
#     count+=1
# print(min(participant))
dic = dict()
for i in range(par):
    key = "k"+str((i+1))
    val = int(input("For "+key))
    val = bfs1.getstep(pos,con,inp,lastpos,val)
    print('for',i)
    print(bfs1.visited)
    dic[key]= val
#dic = dic.sort()
print(dic,min(dic.values()))