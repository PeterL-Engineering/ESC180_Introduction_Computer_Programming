def haul_kid_house(hh, house, kid):
    '''Return the number of items kid kid collected 
    in house house'''
    if not kid in hh[house]:
        return 0
    else:
        return len(hh[house][kid])

def haul_kid(hh, kid):
    total = 0
    for house, house_dict in hh.items():
        total +=haul_kid_house(hh, house, kid)
    return total

def luckiest_kid(hh):
    '''Want to make a dictionary
    haul[kid] = haul for the kids 
    
    want a list of all the kids
    
    To get a list of all the kids, go through
    each house dict, extract the keys'''

    all_kids = []

    for house, house_dict in hh.items():
        for kid, haul in house_dict.items():
            all_kids.append(kid)

    haul = {}
    for kid in all_kids:
        haul[kid] = haul_kid(hh, kid)
    
    cur_luckiest_kid = "Roger"
    cur_max_items = -1
    for kid, num_items in haul.items():
        if cur_max_items < num_items:
            cur_max_items = num_items
            cur_luckiest_kid = kid
    return cur_luckiest_kid