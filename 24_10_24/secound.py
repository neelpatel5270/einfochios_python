n1 = int(input("Enter The Strting Range: "))
n2 = int(input("Enter The Ending Range: "))
sum=0
n1 =+1
for r in range(n1,n2):
    if r%2!=0:
        sum = sum+r
print("Sum in Odd Number: ",sum)