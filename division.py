def Divisible():
    x = int(input("Input your first number here "))
    y = int(input ("Input your second number here "))
    divided = x / y
    decimal = x % y
    if decimal == 0:
            print (x, "divided by",y, "is equal to",divided)
    if decimal != 0:
            print ("The numbers", x, "and", y, "are not divisible")
    
