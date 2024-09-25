def get_hedons_per_min(activity):
    if activity == "jumping":
        hedons_per_min = 1
    elif activity == "swimming" and (cur_minutes - last_non_rest >= 60):
        hedons_per_min = 2
    else:
        hedons_per_min = 0
    return hedons_per_min

#cur_minutes = 0
# jump for 5 minutes
## cur minutes is now 
# time of last non rest activity is 5
# rest for 2 minutes
## cur miutes is now 7
# time of end of last non rest activity is 5

def perform_activity(activity, duration):
    global cur_hedons
    global cur_minutes
    global last_non_rest
    hedons_per_min = get_hedons_per_min(activity)

    cur_hedons = cur_hedons + hedons_per_min * duration
    cur_minutes = cur_minutes + duration
    if activity != "resting":
        last_non_rest = cur_minutes

    #a = a + b is the same as a += b
def print_cur_hedons():
    print("Current hedons:", cur_hedons)

def initialize():
    global cur_hedons
    global cur_minutes
    global last_non_rest
    cur_minutes = 0
    cur_hedons = 0
    last_non_rest = -100

#def initialize resets the variables so that you can run a new simulation

if __name__=='__main__':
    cur_hedons = 0
    cur_minutes = 0
    last_non_rest = -100
    #Keep track of the end of the last non-rest activity
    perform_activity("jumping", 13) # 13 hedons # 13 minutes
    perform_activity("resting", 7) # 0 hedons # 20 minutes
    perform_activity("swimming", 1) # 2 hedons # 21 minutes
    print_cur_hedons()
    # cur_hedons should be 13