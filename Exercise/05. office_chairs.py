# First way from the Lector

def check_the_rooms(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
        free_chairs += difference
    return free_chairs
 
 
count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")

# Second way from me 

rooms = int(input())
total_free_chairs = 0
for room in range(1,rooms + 1):
    needed_chairs_in_room = 0
    current_room = input().split()
    chair_in_room = current_room[0]
    visitors_in_room = current_room[1]
    if len(chair_in_room) == int(visitors_in_room):
        continue
    elif len(chair_in_room) > int(visitors_in_room):
        total_free_chairs += len(chair_in_room) - int(visitors_in_room)
    elif len(chair_in_room) < int(visitors_in_room):
        needed_chairs_in_room = int(visitors_in_room) - len(chair_in_room)  
        if needed_chairs_in_room: 
            print(f"{needed_chairs_in_room} more chairs needed in room {room}")

if needed_chairs_in_room <= 0:
    print(f"Game On, {total_free_chairs} free chairs left")