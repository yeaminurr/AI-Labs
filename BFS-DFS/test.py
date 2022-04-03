queue = [1]
f=100
inp = list()
'''while f>0:
    for i in queue:
        queue.pop(0)
        queue.append("1")
        #print("done")
        break
        break'''

file= open("input1.txt")
count = 0
for i in file:
    i = i.rstrip()
    if count==0:
        pos = int(i)
    elif count == 1 :
        con = int(i)
    elif count==con+2:
        lunapos = int(i)
    else:
        inp1 = i.split(" ")
        inp1[0]= int(inp1[0])
        inp1[1] = int(inp1[1])
        inp.append(inp1)
    count+=1



print(pos,con,lunapos)
print(inp)
