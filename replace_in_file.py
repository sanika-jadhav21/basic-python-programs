# replace python to java

with open("Practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file I/O ")
    f.write("\nusing python \nI like programin in python")

with open("Practice.txt", "r") as f:
    data = f.read()
    print("Original data:")
    print(data)

new_data = data.replace("python", "java")
print("Modified data:")
print(new_data)

with open("Practice.txt", "w") as f:
    f.write(new_data)
