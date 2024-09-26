def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_non_rest
    global bored_with_stars

    global cur_star
    global cur_star_activity
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None # Integer value
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_non_rest = -1000
    
def star_can_be_taken(activity):
    global bored_with_stars
    
    if cur_star / cur_time > 1.5: #still confused about how the star was offered for activity "activity"
        bored_with_stars = True
        return False
    else:
        return True

def get_hedons_per_min(activity):
    if activity == "running" and  (cur_time - last_non_rest >= 120):
        hedons_per_min = 2
    elif activity == "textbooks" and  (cur_time - last_non_rest >= 120):
        hedons_per_min = 1
    elif activity == "running" or "textbooks" and  (cur_time - last_non_rest < 120):
        hedons_per_min = -2
    else:
        hedons_per_min = 0
    return hedons_per_min

def perform_activity(activity, duration):
    global cur_hedons
    global cur_health
    global cur_star_activity
    
    global last_activity
    global last_activity_duration
    
    global cur_time
    global last_non_rest

    if activity == "resting":
       last_activity = activity
       last_activity_duration = duration
       cur_time += duration

    elif activity == "running":
        last_activity = activity
        last_activity_duration = duration

        hedons_per_min = get_hedons_per_min(activity)
        if cur_star_activity != "running":
            if duration <= 10:
                cur_hedons += duration * hedons_per_min #hedons_per_min for running = 2
                cur_health += duration * 3
                cur_time += duration
                last_non_rest = cur_time
            elif duration <= 180:
                cur_hedons += (hedons_per_min * 10) + (duration - 10) * -2 #hedons_per_min * 10 represents if duration <= 10, add to duration - 10 because if less than 10 is different than less than 180
                cur_health += duration * 3 
                cur_time += duration
                last_non_rest = cur_time
            else:
                cur_hedons += (hedons_per_min * 10) - (duration - 10) * -2 #same as above because same limitations on hedons
                cur_health += 540 + (duration - 180) # 3 * 180 =540 for the health points above, get 1 health point for every minute after 180
                cur_time += duration
                last_non_rest = cur_time
        else: #cur_star_activity == "running"
            if duration <= 10:
                cur_hedons += duration * 5 #3 hedons/min with star, 2 hedons/min regular
                cur_health += duration * 3
                cur_time += duration
                last_non_rest = cur_time
            elif duration <= 180:
                cur_hedons += 50 + (duration - 10) * -2 #50 because 5 x 10 for initial star hedons
                cur_health += duration * 3
                cur_time += duration
                last_non_rest = cur_time
            else:
                cur_hedons += 50 - (duration - 10) * -2
                cur_health += 540 + (duration - 180)
                cur_time += duration
                last_non_rest = cur_time           
                
    else: #now on final activity for the function perform activity. textbooks
        last_activity = activity
        last_activity_duration = duration

        hedons_per_min = get_hedons_per_min(activity)

        if cur_star_activity != "textbooks":
            if duration <= 20:
                cur_hedons += duration * hedons_per_min
                cur_health += duration * 2
                cur_time += duration
                last_non_rest = cur_time
            else:
                cur_hedons += 20 + (duration - 20) * -1 #hedons_per_min * 20 for above
                cur_health += 40 + (duration - 20) * 2
                cur_time += duration
                last_non_rest = cur_time
        else: #cur_star_activity = "textbooks"
            if duration <= 10: 
                cur_hedons += duration * 3
                cur_health += duration * 2
                cur_time += duration
                last_non_rest = cur_time        
            if duration <= 20:
                cur_hedons += 30 + (duration - 10) * hedons_per_min #30 + duration bc of stars 
                cur_health += duration * 2
                cur_time += duration
                last_non_rest = cur_time
            else:
                cur_hedons += 30 + hedons_per_min * 10 + (duration - 20) * -1
                cur_time = cur_time + duration
                last_non_rest = cur_time    
        
    cur_star_activity = None

def get_cur_hedons():
    return cur_hedons
    
def get_cur_health():
    return cur_health
    
def offer_star(activity):
    global cur_star_activity
    global bored_with_stars

    if star_can_be_taken == True:
        cur_star_activity = activity
    else:
        return print("User is bored with stars!")
   
def most_fun_activity_minute():
    if last_activity == "resting": #wait can we not do running right after textbooks 
        return "running"
    elif cur_star_activity == "running":
        return "running"
    elif cur_star_activity == "textbooks":
        return "textbooks"
    else:
        return "resting"
    
################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            
def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("resting", 20)
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10

#how will stars affect get_hedons_per_min and most_fun_activity
