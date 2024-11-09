# Reverse an input string and print it


with open("input.txt", "w") as file:
    content = input("Enter the text to write into the file: ")
    file.write(content)


with open("input.txt", "r") as file:
    content = file.read()
    reversed_content = content[::-1]  

print("Reversed content:",reversed_content)
