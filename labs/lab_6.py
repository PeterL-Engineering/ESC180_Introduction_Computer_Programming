'''
#Question 1

L = [["CIV", 92],
["180", 98],
["103", 99],
["194", 95]]

print(L[2][1])

#Question 2

def get_nums(L):
    res = []
    for row in range(len(L)):
        res.append(L[row][1])

    return res

print(get_nums(L))

#Question 3

def lookup(L, num):
    for i in range(len(L)):
        if L[i][1] == num:
            return L[i][0]
        
    return None

print(lookup(L, 97))
'''
#Question 4

#a)
'''When x0 * x1 is greater than 0 ie positive, 
the x's have no impact on direction/sign of the energy, 
therefore we can look at the weight independently.
 When we do this, we find that weight has an inverse relationship with energy. 
 So, when weight increases, energy decreases  '''

#b)

def E(x0, x1, x2, w01, w02, w12):

    term1 = x0 * x1 * w01
    term2 = x0 * x2 * w02
    term3 = x1 * x2 * w12
    
    return -(term1 + term2 + term3)

def print_all_energies(w01, w02, w12):

    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                if x0 * x1 > 0:
                    w01 += 0.1
                else:
                    w01 -= 0.01

                if x0 * x2 > 0:
                    w02 += 0.1
                else:
                    w02 -= 0.01

                if x1 * x2 > 0:
                    w12 += 0.1
                else:
                    w12 -= 0.01
                print("x: (", x0, x1, x2, ")", "E:", E(x0, x1, x2, w01, w02, w12))
        
    return [w01, w02, w12, x0, x1, x2]

def loop_print(n, w01, w02, w12):
    for i in range(n):
        var = print_all_energies(w01, w02, w12)
        w01 = var[0]
        w02 = var[1]
        w12 = var[2]
        print("=================")

    return [w01, w02, w12, var[3], var[4], var[5]]


if __name__ == '__main__':

    w01 = 2
    w02 = -1
    w12 = 1
    arr = loop_print(6, w01, w02, w12)

#Question 5


 