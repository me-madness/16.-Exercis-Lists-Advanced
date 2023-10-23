# First way from the Lector



# Second way from me 

list_with_exercise = input().split(", ")

while True:


    commands = input().split(":")
    command = commands[0]
    index_one = commands[1]
    if command == "course start":
        break
    elif command == "Add":
        list_with_exercise.append(index_one)
    elif command == "Insert":
        index_two = commands[2]
        list_with_exercise.insert(index_two, index_one)
    elif command == "Remove":
        list_with_exercise.remove(index_one)
    elif command == "Swap":
        pass
    elif command == "Exercise":
        pass    

lesson_index = (exercise for exercise in range(list_with_exercise))    
print(f"{lesson_index}.{list_with_exercise}")  

# Data Types, Objects, Lists
# Add:Databases
# Insert:Arrays:0
# Remove:Lists
# course star