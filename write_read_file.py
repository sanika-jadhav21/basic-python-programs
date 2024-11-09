# Open or create a file in append mode

f = open("Hello.txt", "a")
 #f = open("Hello.txt", "r+") ---->overwrite 
f.write("Hello")
f.write("\nI am Sanika Rajendra Jadhav")
f.close()

# Reading the file content to verify what was written
with open("Hello.txt", "r") as f:
    content = f.read()
    print("File content:")
    print(content)
