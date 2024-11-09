#Count the number of words in an input string.

with open("input.txt", "w") as file:
    content = input("Enter the text to write into the file: ")
    file.write(content)


with open("input.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())  

print(f"The number of words in the file is: {word_count}")

