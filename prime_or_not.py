# Checking no. is prime or not 

n = int(input("Enter a number: "))      

def is_prime(n):
    
    if n <= 1:
        print("is not a prime number.") 
    elif n == 2 or n == 3:
        print("is a prime number.")
        return     
    else:
        for i in range(2, n):
            if n % i == 0:
                print("is not a prime number.")
                return 

    print("is prime number")
          
is_prime(n)
