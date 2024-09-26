#Question 1

def parrot_trouble(talking, hour):
  if talking == False and (hour >= 7 or hour <= 20):
    return False
  elif talking == True and (hour == 20 or hour == 7):
    return False
  else:
    return True
  
def sum_double(a, b):
    if a != b:
        return a + b
    else:
        return 2 * (a + a)

def sleep_in(weekday, vacation):
  if weekday != True or vacation != False:
    return True
  else:
    return False
  
def set_square(x):
   global ret_square

   ret_square = x * x
   

if __name__ == '__main__':
   ret_square = 0
