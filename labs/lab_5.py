#Question 1

def count_evens(L):
    num_evens = 0
    for num in L:
        if num % 2 == 0:
            num_evens += 1

    return num_evens

#Question 2

def list_to_strs(lis):
    output = ""
    for word in lis:
        output += "word",

    return lis

#Question 3

def lists_are_the_same(list1, list2):
    for i in range (len(list1)):
            if list1(i) != list2(i):
                return False
    else: return True

#Question 4

def list1_start_with_list2(list1, list2):
    if len(list1) < len(list2):
        return False
    else:
        for i in range (len(list1)):
                if list1(i) != list2(i):
                    return False
        return True
    
#Question 5

def match_pattern(list1, list2):
    for i in range (len(list1) - len(list2)):
        did_not_match = False
        for j in range (len(list2)):
             if list1(i+j) != list2(j):
                did_not_match = True
        
        if did_not_match == True:
             continue
        
        else:
             return True
    
    return False

#Question 6

def duplicates(list0):
    for i in list0:
          if list(i) == list(i+1):
               return True
    return False

#Question 7

#part a)
time_list = [1, 2, 3, 4, 5, 6, 7]
position_list = [1, 2, 3, 4, 5, 6, 7]

def estimate_velocity(time):
    time_index = time_list.index(time)
    position_index = time_index

    if time_index - 1 < 0:
        print("ERROR: CANNOT COMPUTE VELOCITY") 
    
    elif time_index -2 < 0:
        velocity = (position_list(position_index + 1) - position_list(position_index - 1))/(time_list(time_index + 1) - time_list(time_index - 1))

        return velocity

    elif time_index + 1 > len(time_list) + 1:
        print("ERROR: CANNOT COMPUTE VELOCITY") 

    elif time_index + 2 < len(time_list) + 1:
        velocity = (position_list(position_index + 1) - position_list(position_index - 1))/(time_list(time_index + 1) - time_list(time_index - 1))

        return velocity    

    else:
        velocity_a = (position_list(position_index + 1) - position_list(position_index - 1))/(time_list(time_index + 1) - time_list(time_index - 1))
        velocity_b = (position_list(position_index + 2) - position_list(position_index - 2))/(time_list(time_index + 2) - time_list(time_index - 2))
        velocity = (velocity_a + velocity_b)/2

        return velocity
    
#part b)
import random

def add_noise():
    for i in time_list:
        i += 0.1*random.randint(1,11)
    for j in position_list:
        j += 0.1*random.randint(1,11)