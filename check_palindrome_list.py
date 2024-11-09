# checking palindrome or not 

list1=[1,2,3]


copied_list1=list1.copy()
print("copied list1:",copied_list1)

copied_list1.reverse()
print("reverse list1 :",copied_list1)


if(copied_list1==list1): 
    print("palindrome")
else:
    print("not palindrome")
