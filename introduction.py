
cy1 = int(input("Enter the first cyclist's speed"))
cy2 = int(input("Enter the second cyclist's speed"))
cy3 = int(input("Enter the third cyclist's speed"))

avg = (cy1+cy2+cy3)//3
print("The average is ", avg)

if avg>cy1 and avg>cy2 and avg>cy3:

    print("Average is greater than all")

elif avg>cy1 and avg>cy2:

    print("Average is greater than cyclist 1 and cyclist 2")

elif avg>cy1 and avg>cy3:

    print("Average is greater than cyclist 1 and cyclist 3")

elif avg>cy2 and avg>cy3:

    print("Average is greater than cyclist 2 and cyclist 3")

elif avg>cy1 :

    print("Average is only greater than cyclist 1")

elif avg>cy2 :

    print("Average is only greater than cyclist 2")

elif avg>cy3 :

    print("Average is only greater than cyclist 3")

elif avg==cy1 :

    print("Average is equal to cyclist 1")

elif avg==cy2 :

    print("Average is equal to cyclist 2")

elif avg==cy3 :

    print("Average is equal to cyclist 3")

else:

    print("Invalid input!")