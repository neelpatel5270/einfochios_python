mylist=[]
sum=0
count = 0
while count<10:
    count+=1
    n1 = input("Enter The Number or string : ")

    try:
        n2 = int(n1)
        sum = sum+n2
    except:
        mylist.append(n1)

print("Sum of all Digit: ",sum)
print(mylist)
print(count)
