print( "Welcome to calculator project")
print( "1. Addition")
print( "2. Subtraction")
print( "3. Multiplication")
print( "4. Divition")

option =int(input("select an option: ")) 
if option == 1:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = n1 + n2
    print (" Addition is: " + str(n3))
elif option == 2:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = n1 - n2
    print ("Subtraction is: " + str(n3))
elif option == 3:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = n1 * n2
    print ("Multiplication is: " + str(n3))
elif option == 4:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = n1 / n2
    print ("Divition is: " + str(n3))
else:
    print("invalid input")    