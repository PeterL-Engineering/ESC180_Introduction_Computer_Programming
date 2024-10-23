passwords = {"yip": "coffee", "bentz": "milk", "guerzhoy": "coffee"}

def lookup_users_by_password(passwords, pwd):
    res = []
    # Return a list of users whose password is pwd
    for user, pwd0 in passwords.items():
        if pwd == pwd0:
            res.append(user)
            print("Appended", user, "res is now", res)
    
    return res

def lookup_user_by_password(passwords, pwd):
    #Return a user whose password is pwd
    for user, pwd0 in passwords.items():
        if pwd == pwd0:
            return user 

#Q.5 From midterm 2022

def count_candy_house(halloween_haul, house, kid):
    #Return the number of candy items the kid named kid got

    return len(halloween_haul[house][kid])

def count_candy(hh, kid):

    res = 0
    for house, house_dict in hh.items():
        res += count_candy_house(hh, kid, house)

def luckiest_kid(hh):
    luckiest_kid_so_far = "Evan Bentz"
    amt_candy = -1

    for house, house_dict in hh.items():
        for kid, haul in house_dict.items():
            kid_haul = count_candy(hh, kid)
            if kid_haul > amt_candy:
                luckiest_kid_so_far = kid
                amt_candy = kid_haul

    return luckiest_kid_so_far


if __name__ == '__main__':
    hh = {"Bahen": {"Annie": ["1", "2"],
                    "Jackie": ["3"]},
         "SF": {"Annie": ["1"],
                   "Jackie": ["5", "6"]}}
    
    count_candy(hh, "Annie")
