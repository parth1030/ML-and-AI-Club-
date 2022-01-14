tb = [[2,0,0],
     [0,2,0],
     [2,0,2]]

def whoWon(t):
    if t[0][0] == 1 and t[0][1] == 1 and t[0][2] == 1:
        return -1
    if t[1][0] == 1 and t[1][1] == 1 and t[1][2] == 1:
        return -1
    if t[2][0] == 1 and t[2][1] == 1 and t[2][2] == 1:
        return -1
    if t[0][0] == 1 and t[1][0] == 1 and t[2][0] == 1:
        return -1
    if t[0][1] == 1 and t[1][1] == 1 and t[2][1] == 1:
        return -1
    if t[0][2] == 1 and t[1][2] == 1 and t[2][2] == 1:
        return -1
    if t[0][0] == 1 and t[1][1] == 1 and t[2][2] == 1:
        return -1
    if t[0][2] == 1 and t[1][1] == 1 and t[2][0] == 1:
        return -1

    if t[0][0] == 2 and t[0][1] == 2 and t[0][2] == 2:
        return 1
    if t[1][0] == 2 and t[1][1] == 2 and t[1][2] == 2:
        return 1
    if t[2][0] == 2 and t[2][1] == 2 and t[2][2] == 2:
        return 1
    if t[0][0] == 2 and t[1][0] == 2 and t[2][0] == 2:
        return 1
    if t[0][1] == 2 and t[1][1] == 2 and t[2][1] == 2:
        return 1
    if t[0][2] == 2 and t[1][2] == 2 and t[2][2] == 2:
        return 1
    if t[0][0] == 2 and t[1][1] == 2 and t[2][2] == 2:
        return 1
    if t[0][2] == 2 and t[1][1] == 2 and t[2][0] == 2:
        return 1
    else:
        return 0

possib_arr = []

def possible(t):
    if t[0][0] == 0:
        possib_arr.append(1)
    if t[0][1] == 0:
        possib_arr.append(2)
    if t[0][2] == 0:
        possib_arr.append(3)
    if t[1][0] == 0:
        possib_arr.append(4)
    if t[1][1] == 0:
        possib_arr.append(5)
    if t[1][2] == 0:
        possib_arr.append(6)
    if t[2][0] == 0:
        possib_arr.append(7)
    if t[2][1] == 0:
        possib_arr.append(8)
    if t[2][2] == 0:
        possib_arr.append(9)



def findBiggest(t):
    length_t = len(t)
    for i in range(1, length_t - 1):
        if t[i] < t[i + 1]:
            return i
        elif t[i] > t[i + 1]:
            return i
            break
        else:
            return i
            break


def MiniMax(t):
    MiniMax = []
    for i in range(0,len(possib_arr)-1):
        if possib_arr[i] == 1:
            t[0][0] = 2
            MiniMax.append(whoWon(t))
            t[0][0] = 0
        if possib_arr[i] == 2:
            t[0][1] = 2
            MiniMax.append(whoWon(t))
            t[0][1] = 0
        if possib_arr[i] == 3:
            t[0][2] = 2
            MiniMax.append(whoWon(t))
            t[0][2] = 0
        if possib_arr[i] == 4:
            MiniMax.append(whoWon(t))
            t[1][0] = 0
        if possib_arr[i] == 5:
            t[1][1] = 2
            MiniMax.append(whoWon(t))
            t[1][1] = 0
        if possib_arr[i] == 6:
            t[1][2] = 2
            MiniMax.append(whoWon(t))
            t[1][2] = 0
        if possib_arr[i] == 7:
            t[2][0] = 2
            MiniMax.append(whoWon(t))
            t[2][0] = 0
        if possib_arr[i] == 8:
            t[2][1] = 2
            MiniMax.append(whoWon(t))
            t[2][1] = 0
        if possib_arr[i] == 9:
            t[2][2] = 2
            MiniMax.append(whoWon(t))
            t[2][2] = 0

        biggest = findBiggest(MiniMax)
        print(biggest)
        if biggest == 1:
            t[0][0] = 2
        if biggest == 2:
            t[0][1] = 2
        if biggest == 3:
            t[0][2] = 2
        if biggest == 4:
            t[1][0] = 2
        if biggest == 5:
            t[1][1] = 2
        if biggest == 6:
            t[1][2] = 2
        if biggest == 7:
            t[2][0] = 2
        if biggest == 8:
            t[2][1] = 2
        if biggest == 9:
            t[2][2] = 2

possible(tb)

MiniMax(tb)

for r in tb:
   for c in r:
      print(c,end = " ")
   print()




        








