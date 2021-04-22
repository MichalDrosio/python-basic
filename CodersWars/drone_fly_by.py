def fly_by(lamps, drone):
    d = len(drone)
    t = 'o'*(len(drone))
    if len(lamps) > len(drone):
        return t + lamps[d:]
    return 'o'*len(lamps)


print(fly_by('xxxxxx', '===T'))