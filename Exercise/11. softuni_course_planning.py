# First way from the Lector



# Second way from me 

list_with_exercise = input().split(", ")

while True:
    commands = input().split(":")
    command = commands[0]
    if command == "course start":
        break
    elif command == "Add":
        list_with_exercise.append(command[1])
    elif command == "Insert":
        list_with_exercise.insert(command[2], command[1])
    elif command == "Remove":
        list_with_exercise.remove(command[1])
    elif command == "Swap":
        pass
    elif command == "Exercise":
        pass    

lesson_index = (exercise for exercise in range(list_with_exercise))    
print(f"{lesson_index}.{list_with_exercise}")    