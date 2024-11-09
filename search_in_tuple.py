#search no for x in tuple using loop

num=(9,10,7,6,5,43,91,75,10)
a=int(input("Enter No. to search"))
i=0
while i<len(num):
    if a==num[i]:
       print("no. found , where index is",i)
    else:
        print("not present in tuple")   
    i += 1
