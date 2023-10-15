# First way from the Lector



# Second way from me 

rooms = int(input())
total_free_chairs = 0
for room in range(rooms):
    current_room = input().split()
    chair_in_room = current_room[0]
    visitors_in_room = current_room[1]
    if len(chair_in_room) > visitors_in_room:
        total_free_chairs += 1
        
    print(chair_in_room)
    print(visitors_in_room)
# print("{needed_chairs_in_room} more chairs needed in room {number_of_room}")
print("Game On, {total_free_chairs} free chairs left")