def current_position(x):
    global prev_x
    global prev_velocity

    cur_velocity = (x - prev_x)/0.1
    cur_acc = (cur_velocity - prev_velocity)/0.1
    print("Current coord", x)
    print("Estimated velocity:", cur_velocity)
    print("Estimated acceleration:", cur_acc)

    prev_x = x
    prev_velocity = cur_velocity
