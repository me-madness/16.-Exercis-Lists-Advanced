# First way from the Lector



# Second way from me 

list_with_exercise = input().split(", ")

while True:
    command = input().split(":")
    if command == "course start":
        break
    elif command[0] == "Add":
        list_with_exercise.append(command[1])
    elif command[0] == "Insert":
        list_with_exercise.insert(command[2], command[1])
    elif command[0] == "Remove":
        list_with_exercise.remove(command[1])
    elif command[0] == "Swap":
        pass
    elif command[0] == "Exercise":
        pass    
    
print(f"{list_with_exercise}.{list_with_exercise}")    