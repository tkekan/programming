


def main():
    def maximum_profit():
        global tasks
        tasks = sorted(tasks,key=lambda x: x[2],reverse = True)
        print tasks
        in_use = [False] * len(tasks)
        res = []
        for t in tasks:
            for j in range(min(t[1],len(tasks))-1, -1,-1):
                if in_use[j] == False:
                    in_use[j] = True
                    res.append((t[0],t[2]))
                    break
        print res
    maximum_profit()



tasks = [ ['a', 2, 100], ['b', 1, 19], ['c', 2, 27], 
           ['d', 1, 25], ['e', 3, 15]] 
main()
