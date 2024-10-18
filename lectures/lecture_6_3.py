#How to find the energy minimum of a hopfield network

L = [5, 10,-2]

def E(x0, x1, x2):
    term1 = x0 * x1 * 2
    term2 = x1 * x2 * 1
    term3 = x2 * x0 * -1

    return (term1 +term2 + term3)

def min_list():
    cur_min = L[0]
    cur_min_loc = 0

    for i in range(len(L)):
        if L[i] < cur_min:
            cur_min = L[i]
            cur_min_loc = i
    return cur_min_loc

def print_all_energies():
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                print ("x: ", x0, x1, x2, ")", "E:", E(x0, x1, x2))

def retrieve_x_at_min_energy():

    cur_min_E = E(0, 0, 0)
    cur_min_x0, cur_min_x1, cur_min_x2 = 0, 0, 0

    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                #print ("x: ", x0, x1, x2, ")", "E:", E(x0, x1, x2))
                cur_E = E(x0, x1, x2)
                if cur_E < cur_min_E:
                    cur_min_x0, cur_min_x1, cur_min_x2 = x0, x1, x2

    return(cur_min_x0, cur_min_x1, cur_min_x2)