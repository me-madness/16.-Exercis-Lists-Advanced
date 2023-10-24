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
        index_one = commands[1]
        index_two = commands[2]
        a, b = list_with_exercise.index(index_one), list_with_exercise.index(index_two)
        list_with_exercise[b], list_with_exercise[a] = list_with_exercise[a], list_with_exercise[b]
    elif command == "Exercise":
        index_one = command[1]
        for exercise in list_with_exercise:
            if exercise == index_one:
                exercise = (exercise + "-" + "Exercise")
            else:
                list_with_exercise.append(index_one + "-" + "Exercise")        


for exercise in list_with_exercise:
    lesson_index += 1   
    print(f"{lesson_index}.{exercise}")  


# "Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
# a, b = i.index('password2'), i.index('password1')
# i[b], i[a] = i[a], i[b]

# "Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index, 
# if the lesson exists and there is no exercise already, in the following format 
# "{lessonTitle}-Exercise". If the lesson doesn't exist, add the lesson at the end of 
# the course schedule, followed by the Exercise.

## First input

# Data Types, Objects, Lists
# Add:Databases
# Insert:Arrays:0
# Remove:Lists
# course start

## Second input

