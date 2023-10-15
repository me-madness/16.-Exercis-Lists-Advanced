# First way from the Lector

words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_words))

# Second way from me 

text = input().split(" ")
new_text = [text_one for text_one in text if len(text_one) % 2 == 0]
print("\n".join(new_text))