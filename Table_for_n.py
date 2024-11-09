# Multiplication Table for given Number 

n=int(input("Enter Number:"))

def Multiplication(n):
    for i in range(1,11,):
        print(i,"*",n,"=",i*n)
        i+=1

Multiplication(n)
