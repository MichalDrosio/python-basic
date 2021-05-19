def calculate_paint(efficency_ltr_per_m2, **number_of_rooms):
    result = 0
    for room, meters in number_of_rooms.items():
        result += meters * efficency_ltr_per_m2

    return result

print(calculate_paint(10, room1=10, room2=15, room3=9))