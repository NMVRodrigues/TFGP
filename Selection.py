import Node


def tournament(parents, popsize, tsize):
    chosen = []
    while(len(chosen) < popsize):
        r = [rand.randint(0,popsize-1) for x in range(0,tsize)]
        chosen.append(parents[min(r)])
    return chosen


def doubleTournament(parents, popsize):
    chosen = []
    parents = sorted(parents, key=lambda x: x[2])
    #print("sorted: ", '\n')
    #for i in parents:
    #    print(i[2])
    while (len(chosen) < popsize):
        r = [rand.randint(0, popsize - 1) for x in range(0, 2)]
     #   print("first: ", parents[r[0]][2])
     #   print("second: ", parents[r[1]][2])
        if rand.random() < D:
      #      print("choice: ", parents[min(r)][2], '\n')
            chosen.append(parents[min(r)])
        else:
       #     print("choice: ", parents[max(r)][2], '\n')
            chosen.append(parents[max(r)])
    chosen = sorted(chosen, key=lambda x: x[1])
    return chosen