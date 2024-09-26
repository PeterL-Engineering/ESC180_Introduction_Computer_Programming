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

    cur_star = 0 # Integer value
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_non_rest = -1000

def star_can_be_taken(activity):
    global bored_with_stars
    global cur_star
    global cur_time

    if cur_time != 0 and cur_star / cur_time > 1.5: #still confused about how the star was offered for activity "activity"
        bored_with_stars = True
        cur_star = 0
        return True
    elif cur_time == 0:
        cur_star = 0
    else:
        cur_star += 1
        return False

def get_hedons_per_min(activity):
    if activity == "running" and  (cur_time - last_non_rest >= 120):
        hedons_per_min = 2
    elif activity == "textbooks" and  (cur_time - last_non_rest >= 120):
        hedons_per_min = 1
    else:
        hedons_per_min = -2
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
       cur_time += duration
    elif activity == "running":
        hedons_per_min = get_hedons_per_min(activity)
        if cur_star_activity != "running":
            if last_activity != "running":
                if duration <= 10:
                    cur_hedons += duration * hedons_per_min
                    cur_health += duration * 3
                    cur_time += duration
                    last_non_rest = cur_time
                elif duration <= 180:
                    cur_hedons += 10 * hedons_per_min + (duration - 10) * -2
                    cur_health += duration * 3
                    cur_time += duration
                    last_non_rest = cur_time
                else:
                    cur_hedons += 10 * hedons_per_min + (duration - 10) * -2
                    cur_health += 540 + (duration - 180)
                    cur_time += duration
                    last_non_rest = cur_time
            elif last_activity_duration < 180:
                if duration <= 10:
                    cur_hedons += duration * hedons_per_min
                    cur_health += (180 - last_activity_duration) * 3
                    cur_time += duration
                    last_non_rest = cur_time
                elif duration <= 180:
                    cur_hedons += 10 * hedons_per_min + (duration - 10) * -2
                    cur_health += (180 - last_activity_duration) * 3 + (180 - duration)
                    cur_time += duration
                    last_non_rest = cur_time
                else:
                    cur_hedons += duration
                    cur_health += 540 + (duration - 180)
                    cur_time += duration
                    last_non_rest = cur_time

        else: #cur_star_activity == "running"
            if duration <= 10:
                cur_hedons += duration * (hedons_per_min + 3) 
                cur_health += duration * 3
                cur_time += duration
                last_non_rest = cur_time
            elif duration <= 180:
                cur_hedons += 10 * (hedons_per_min + 3) + (duration - 10) * -2 
                cur_health += duration * 3
                cur_time += duration
                last_non_rest = cur_time
            else:
                cur_hedons += 10 * (hedons_per_min + 3) + (duration - 10) * -2 
                cur_health += 540 + (duration - 180)
                cur_time += duration
                last_non_rest = cur_time

    else: #now on final activity for the function perform activity. textbooks

        hedons_per_min = get_hedons_per_min(activity)

        if cur_star_activity != "textbooks":
            if duration <= 20:
                cur_hedons += duration * hedons_per_min
                cur_health += duration * 2
                cur_time += duration
                last_non_rest = cur_time
            elif last_activity == "running" or "textbooks" and cur_time - last_non_rest > 120:
                cur_hedons +=  20 * hedons_per_min + (duration - 20) * -1 #hedons per min is either -1 or -2
                cur_health += duration * 2
                cur_time = cur_time + duration
                last_non_rest = cur_time
            else:
                cur_hedons +=  20 * hedons_per_min + (duration - 20) * -2 #hedons per min is either -1 or -2
                cur_health += duration * 2
                cur_time = cur_time + duration
                last_non_rest = cur_time
        else: #cur_star_activity = "textbooks"
            if duration <= 20:
                cur_hedons += duration * (hedons_per_min + 3) 
                cur_health += duration * 2
                cur_time += duration
                last_non_rest = cur_time
            elif last_activity == "running" or "textbooks" and cur_time - last_non_rest > 120:
                cur_hedons +=  20 * (hedons_per_min + 3) + (duration - 20) * -1 #hedons per min is either -1 or -2
                cur_health += duration * 2
                cur_time = cur_time + duration
                last_non_rest = cur_time
            else:
                cur_hedons +=  20 * (hedons_per_min + 3) + (duration - 20) * -2
                cur_health += duration * 2
                cur_time = cur_time + duration
                last_non_rest = cur_time
    if last_activity == activity:
        last_activity_duration += duration
    else:
        last_activity_duration = duration
    
    last_activity = activity
    cur_star_activity = None

def get_cur_hedons():
    return cur_hedons

def get_cur_health():
    return cur_health

def offer_star(activity):
    global cur_star_activity
    global bored_with_stars

    star_can_be_taken(activity)

    if bored_with_stars == False:
        cur_star_activity = activity
    else:
        cur_star_activity = None

def most_fun_activity_minute():
    if last_activity == "resting": #wait can we not do running right after textbooks
        return "running"
    elif cur_star_activity == "running":
        return "running"
    elif cur_star_activity == "textbooks":
        return "textbooks"
    else:
        return "resting"


if __name__ == '__main__':
    initialize()
    offer_star("running")
    perform_activity("resting", 20)
    perform_activity("running", 30)
    get_cur_hedons()            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    get_cur_health()            # 90 = 30 * 3                          # Test 2
    most_fun_activity_minute()  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    most_fun_activity_minute()  # running                              # Test 4
    perform_activity("textbooks", 30)
    get_cur_health()            # 150 = 90 + 30*2                      # Test 5
    get_cur_hedons()            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    get_cur_health()            # 210 = 150 + 20 * 3                   # Test 7
    get_cur_hedons()            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    get_cur_health()            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    get_cur_hedons()            # -430 = -90 + 170 * (-2)              # Test 10
