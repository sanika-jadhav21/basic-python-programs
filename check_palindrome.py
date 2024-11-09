# check palindrome or not  

n = input("Enter word or number: ")

copied_n = n[::-1]

print("Original input:", n)
print("Reversed input:", copied_n)


if copied_n == n:
    print("Palindrome")
else:
    print("Not a palindrome")
