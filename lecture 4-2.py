
def print_n_times(N, s):
    ''' print the string s N times'''
    for i in range (N):
        print(s)

if __name__=='main__':
    #print_n_times(1000, "authority")
    
    '''
    N = 100
    for i in range(N):
        print("RIGOUR")
        '''
    A = 3
    B = 5
    #0 + 3 + 3 + 3 + 3 + 3
    my_sum = 0
    #add 3 into my_sum 5 times
    for i in range(5):
        my_sum += 3
    #my sum will be 15 after the loop ended

    my_sum = 0
    for i in range(B):
        my_sum += A