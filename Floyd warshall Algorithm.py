INF = 999


def Print_solution(g1):
    for i in range(len(g1)):
        for j in range(len(g1)):
            if g1[i][j] == 999:
                print('INF',end=" ")
            else:
                print(g1[i][j],end=" ")
        print()

def floyds_warshalls_algo(g1):
    for k in range(len(g1)):
        for i in range(len(g1)):
            for j in range(len(g1)):
                if g1[i][j] > g1[i][k] + g1[k][j]:
                    g1[i][j] = g1[i][k] +g1[k][j]

    Print_solution(g1)


g1 = [
    [0,8,INF,1],
    [INF,0,1,INF],
    [4,INF,0,INF],
    [INF,2,9,0]

]


print("First")
Print_solution(g1)
