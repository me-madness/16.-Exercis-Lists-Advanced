# First way from the Lector

first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []
for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)
 
#1.1
first_sequence = input().split(", ")
second_sequence = input().split(", ")
print([first_string for first_string in first_sequence if any(first_string in second_string for second_string in second_sequence)])
 


# Second way from me    