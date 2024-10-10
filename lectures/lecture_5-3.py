#Lists

L = ["Bentz", "Guerzhoy", "Carrick"]
L[0] # "Bentz"
L[1] # "Guerzhoy"
len(L) # the length of the list # 3

L[len(L) - 1 ]   # how to access the last element?
 
#Printing a complete list

for e in L:
   print(e)


for i in range(len(L)):
  print(L[i])

L = [12, 1, 3, 56, 2, 17]
number_of_odd_numbers = 0

def odd_number_counter():
   for e in L:
      if e / 2 == int:
         number_of_odd_numbers += 1
    
#Solution

def n_of_odd_numbers():
   for num in L:
      if num % 2 == 1:
         total_odds += 1
   return total_odds

#Check password function

def check_password(username, password):
    global failed_logins

    if failed_logins == 3:
        return False
    
    is_match = user_password_match(username, password, usernames, passwords)

    if not is_match: #ie. if is_match == False
       failed_logins += 1
       return False
    else:
       failed_logins = 0
       return True
    
def get_index(L, e):
   '''Return the index of element e in L'''
   '''Return -1 if element e is not in L'''
   for i in range(len(L)):
      if L[i] == e:
        return 1
   return -1

def user_password_match(username, password, usernames, passwords):
    username_ind = get_index(usernames, username)
    if username_ind == -1:
        return False
    return passwords[username_ind] == password

if __name__ == '__main__':

    usernames = ["gerzhoy", "bentz", "yip", "carrick"]
    passwords = ["blah", "abc", "def", "gji"]
    #The password for usernames[1] is passowrds[1]

    failed_logins = 0

    check_password("guerzhoy", "password") #True
    check_password("bentz", "password") #False
    check_password("bentz", "password") #False
    check_password("bentz", "password") #False
    check_password("guerzhoy", "password") #False
