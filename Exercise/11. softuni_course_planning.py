# First way from the Lector



# Second way from me 

list_with_exercise = input().split()
command = input().split()
while command != "course start":
    if command[0] == "Add":
        list_with_exercise.pop(command[1])
    elif command[0] == "Insert":
        
    elif command[0] == "Remove":
        pass
    elif command[0] == "Swap":
        pass
    elif command[0] == "IExercise":
        pass    
    
print(f"{lesson_index}.{lessonTitle}")    