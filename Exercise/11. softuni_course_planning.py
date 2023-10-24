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
        if index_one not in list_with_exercise:
            list_with_exercise.insert(int(index_two), index_one)
    elif command == "Remove":
        index = commands[1]
        list_with_exercise.remove(index_one)
    elif command == "Swap":
        index_one = commands[1]
        index_two = commands[2]
        if index_one not in list_with_exercise:
            list_with_exercise.append(index_one)
        if index_two not in list_with_exercise:
            list_with_exercise.append(index_two)    
        a, b = list_with_exercise.index(index_one), list_with_exercise.index(index_two)
        list_with_exercise[b], list_with_exercise[a] = list_with_exercise[a], list_with_exercise[b]
    elif command == "Exercise":
        new_value = commands[1]
        if new_value in list_with_exercise:
            a = list_with_exercise.index(new_value + "-" + "Exercise")
        else:
            list_with_exercise.append(new_value + "-" + "Exercise")    

for exercise in list_with_exercise:
    lesson_index += 1   
    print(f"{lesson_index}.{exercise}")  

## First input
# Data Types, Objects, Lists
# Add:Databases
# Insert:Arrays:0
# Remove:Lists
# course start

## Second input
# Arrays, Lists, Methods
# Swap:Arrays:Methods
# Exercise:Databases
# Swap:Lists:Databases
# Insert:Arrays:0
# course start