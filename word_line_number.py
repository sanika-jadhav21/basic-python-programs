# print Line number of that word if exist,otherwise -1

with open("Practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file I/O ")
    f.write("\nusing python \nI like programin in python")

def check_word():
    word="learnig"
    data=True 
    line_no=1
    with open("Practice.txt","r") as f:
        while data:
            data=f.readline()
            if (word in data ):
                print(line_no)
                return 
            line_no+=1
            
        return -1
        
print(check_word())  
