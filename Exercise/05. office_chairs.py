# First way from the Lector



# Second way from me 

rooms = int(input())
total_free_chairs = 0
needed_chairs_in_room = 0
for room in range(rooms):
    current_room = input().split()
    chair_in_room = current_room[0]
    visitors_in_room = current_room[1]
    if len(chair_in_room) > int(visitors_in_room):
        total_free_chairs += len(chair_in_room) - int(visitors_in_room)
    elif len(chair_in_room) < int(visitors_in_room):
        needed_chairs_in_room += int(visitors_in_room) - len(chair_in_room)  
        if needed_chairs_in_room: 
            print(f"{needed_chairs_in_room} more chairs needed in room {room}")


print(f"Game On, {total_free_chairs} free chairs left")