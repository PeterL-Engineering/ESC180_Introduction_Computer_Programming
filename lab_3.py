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

#Question 4


def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -100
    last_coffee_time2 = -100

def drink_coffee():
    if current_time - last_coffee_time < 120:
       too_much_coffee == True
    elif last_coffee_time != -100

def study(minutes):

    global knols
    global current_time

    if too_much_coffee == True:
       current_time = current_time + minutes
       return knols
    else:
       if current_time - last_coffee_time == 0:
          current_time = current_time + minutes
          knols = knols + minutes * 10
          return knols
       else:
            current_time = current_time + minutes
            knols = knols + minutes * 5
            return knols

if __name__ == '__main__':
    initialize() # start the simulation
    study(60) # knols = 300
    study(20) # knols = 400
    drink_coffee() # knols = 400
    study(10) # knols = 500
    drink_coffee() # knols = 500
    study(10) # knols = 600
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 600