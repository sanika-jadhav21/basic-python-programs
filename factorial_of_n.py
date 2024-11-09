# WAF to print fctorial of n 

n=int(input("Enter no."))

def print_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)    
    return fact
    
print_fact(n)
