# search learning word 
with open("Practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file I/O ")
    f.write("\nusing python \nI like programin in python")

def check_word():
    with open("Practice.txt","r") as f:
        data=f.read()
        print(data)
    
    if(data.find("learning") !=-1):
        print("Found")
        
    else:
        print("not found")
    
check_word()
