def calculate_speed(distance,time):
    distance = [10,15,20,31]
    times = [0.3,0.5,0.77,1.15]

    speeds = []
# speed = distance/time
# index of distance divided by index of times

    for i in range(4):
        speeds.append(distance[i]/times[i])
    return speeds


calculate_speed(14,2)