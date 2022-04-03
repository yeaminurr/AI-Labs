
pos =int(input("Enter Positions"))
con = int(input("Enter Connections"))
inp = list()
queue = list()
loop = 8
visited= list()

'''for i in range(con):
    inp1 = input()
    inp1 = inp1.split(" ")
    inp.append(inp1)'''
inp = [[0,1],[0,2],[0,3],[1,3],[1,4],[2,3],[3,5],[3,6],[4,8],[4,7],[5,6],[6,7],[7,8]]
lunapos = int(input("Luna's Position?"))
queue.append(0)
step = 1
z=-1
c= dict()
c[0]=0
while loop>0:
    #step+=1


    for i in queue:

        if i == lunapos:
            abcd = 1
            loop = -1
            break
        elif i != lunapos:
            print("dhuksi")
            queue.pop(0)

            visited.append(int(i))
            for j in inp:
                i=int(i)
                if(int(j[0])==i):
                    queue.append(int(j[1]))
                    if j[1] not in visited:
                        c[i] = c.get(i, 0) + 1
                        print(i, c)

            step+=1

            break
print(visited, step)