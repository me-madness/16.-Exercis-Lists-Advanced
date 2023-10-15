# First way from the Lector

text = input().split(" ")
new_text = [text_one for text_one in text if len(text_one) % 2 == 0]
print("\n".join(new_text))

# Second way from me 