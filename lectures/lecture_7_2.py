#Slicing

L = [ 5, 6, 7, 8]

L[1:3] # same as [6, 7]

# Slicing with Seps

L = [5, 6, 7, 8, 9, 10]
L[0:4:2] # same as [L[0], L[2]] # index 0, up to but not including 4, steps of 2

L[4:2:-1]  # [9, 8] # index 4, down to but not including 2, steps of -1
L[4::-1]    # Can leave out beginning and end
               # start from 4, down to the beginning, steps of -1
               # [9, 8, 7, 6, 5]
L[::-1]      # [10, 9, 8, 7, 6, 5]


#Making a slicing function

def slice_list(L, start, end, step):
    res = []
    #build up res using append
    # assume step is positive

    for i in range(start, end, step):
        res.append(L[i])

    return res

#Python Dictionaries

users = ["yip", "bentz"]
passwords = ["coffee", "milk"]

####

passwords = {"yip": "coffee", "bentz": "milk"}
passwords["yip"] # "coffee"
passwords["bentz"] # "milk"

passwords["guerzhoy"] = "grog" # can now retrieve passwords["guerzhoy"]
# "yip", "bentz", and "guerzhoy" are called keys
# "coffee", "milk", and "grog" are called values

#####

passwords = {"yip": "coffee", "bentz": "milk"}

"yip" in passwords  # True: k in d in checks whether key k is in the dictionary d
"wilson" in passwords # False
"coffee" in passwords # False

passwords = {"yip": "coffee", "bentz": "milk"}

for user, password in passwords.items():
   print(user, password)

# prints:
# yip coffee
# bentz milk

passwords = {"yip": "coffee", "bentz": "milk"}
"grog" in passwords.values()   # False
"milk" in passwords.values()   # True


def lookup_users_by_password(passwords, pwd):
   # Return a list of users whose password is pwd

    for user, pwd0 in passwords.items():
        if pwd == pwd0:
            return user