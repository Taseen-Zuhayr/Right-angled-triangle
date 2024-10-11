n = int(input("Enter the number of rows you want : "))

for i in range(n):
        for stars in range(i+1):
            print("*",end="")
        print("\n")