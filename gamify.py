def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars
    
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = -1000
    
def star_can_be_taken(activity):
    pass

def get_hedons_per_min(activity):
    if activity == "running" and  (cur_time - last_finished >= 120):
        hedons_per_min = 2
    elif activity == "textbooks" and  (cur_time - last_finished >= 120):
        hedons_per_min = 1
    elif activity == "running" or "textbooks" and  (cur_time - last_finished < 120):
        hedons_per_min = -2
    else:
        hedons_per_min = 0
    return hedons_per_min

def get_health_per_min(activity, duration):
    pass

def perform_activity(activity, duration):
    global cur_hedons
    global cur_health
    global last_activity
    global last_activity_duration
    global cur_time

    cur_time = cur_time + duration

    hedons_per_min = get_hedons_per_min(activity)





def get_cur_hedons():
    return cur_hedons
    
def get_cur_health():
    return cur_health
    
def offer_star(activity):
    pass
        
def most_fun_activity_minute():
    pass
    
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
'''Putting this here for now cause I think there's a better way to do it

     if activity == "resting":
       last_activity = activity
       last_activity_duration = duration
       cur_time = cur_time + duration

    elif activity == "running":
        last_activity = activity
        last_activity_duration = duration
        cur_time = cur_time + duration
        hedons_per_min = get_hedons_per_min(activity=)
        
        if duration <= 180:
            cur_health = cur_health + duration * 3
        else: 
            cur_health = cur_health + 540 + duration - 180

        if duration <= 10:
            cur_hedons = cur_hedons + duration * 3
        else:
            cur_hedons = cur_hedons + 20 - (duration - 10) * -2  
''' 
