from DFS import dfs
dfs = dfs()
pos = int(input("Enter Positions"))
con = int(input("Enter Connections"))
#lunapos = int(input("Luna's Position?"))
mydic = dict()
startingpos=0
inp = [[0, 6], [1, 2], [1, 5],  [2, 0], [2, 5], [3, 4], [4, 2], [3, 1]]
maxval = 0
for i in range(7):
    #print(f"for {i}")
    newval = dfs.getstep(pos, con, inp, 6, i)
    if maxval<newval:
        maxval = newval
        maxindex=i

print(maxindex)

