class bfs:
    def getstep(self,pos,con,inp,lunapos,startingpos):
        pos = pos
        con = con
        #inp = list()
        queue = list()
        visited = list()

        # for i in range(con):
        #     inp1 = input()
        #     inp1 = inp1.split(" ")
        #     inp.append(inp1)


        queue.append(startingpos)
        step = 0

        while len(queue) != 0:
            i = queue[-1]

            if i == lunapos:
                visited.append(int(i))
                break
            elif i != lunapos:
                #print("dhuksi")

                queue.pop(0)

                visited.append(int(i))
                for j in inp:
                    i = int(i)
                    if (int(j[0]) == i):
                        queue.append(int(j[1]))
            step += 1
        #print('visited node',visited)
        self.visited = visited
        #print(visited)


        return step



