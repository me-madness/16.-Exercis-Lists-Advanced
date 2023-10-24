# First way from the Lector



# Second way from me 

list_with_exercise = input().split(", ")
lesson_index = 0
while True:

    commands = input().split(":")
    command = commands[0]
    if command == "course start":
        break
    elif command == "Add":
        index = commands[1]
        list_with_exercise.append(index)
    elif command == "Insert":
        index_one = commands[1]
        index_two = commands[2]
        list_with_exercise.insert(int(index_two), index_one)
    elif command == "Remove":
        index = commands[1]
        list_with_exercise.remove(index_one)
    elif command == "Swap":
        pass
    elif command == "Exercise":
        pass    


# lesson_index = (exercise for exercise in len(list_with_exercise)) 
for exercise in list_with_exercise:
    lesson_index += 1   
print(f"{lesson_index}.{exercise}")  

# Data Types, Objects, Lists
# Add:Databases
# Insert:Arrays:0
# Remove:Lists
# course start