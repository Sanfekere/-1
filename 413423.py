r,k = 3,4
burti = [[None] * k for i in range(r)]

burti[0][0] = 'a'
burti[0][1] = 'b'
burti[0][2] = 'c'
burti[0][3] = 'd'
burti[1][0] = 'e'
burti[1][1] = 'f'
burti[1][2] = 'g'
burti[1][3] = 'h'
burti[2][0] = 'i'
burti[2][1] = 'j'
burti[2][2] = 'k'
burti[2][3] = 'l'


for i in range(3):
    for i in range(4):
        print(burti[i][k])
        k +=1
    i += 1
    k = 0
