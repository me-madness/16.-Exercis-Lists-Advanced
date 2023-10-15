# First way from the Lector

def positive_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) >= 0])
 
 
def negative_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) < 0])
 
 
def even_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) % 2 == 0])
 
 
def odd_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) % 2 != 0])
 
 
numbers = input().split(", ")
print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")

# Second way from me 

numbers = input().split(", ")
positive_numbers = [positive for positive in numbers if int(positive) >= 0]
negative_numbers = [negative for negative in numbers if int(negative) < 0]
even_numbers = [even for even in numbers if int(even) % 2 == 0]
odd_numbers = [odd for odd in numbers if not int(odd) % 2 == 0]
print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")