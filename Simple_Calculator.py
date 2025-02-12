#SIMPLE CALUCLATOR PROJECT
#addition 
def Addition(x,y):
    return x+y 
#subtration
def Subtraction(x,y):
    return x-y 
#multilication
def Multiplication(x,y):
    return x*y
#division
def Division(x,y):
    if y==0:
        return "Error not divisible by zero"
    else:
        return x/y
#modulo division
def ModuloDivision(x,y):
    return x % y

def CALUCLATOR():
    print("Select operation")
    print("1.ADD(+)")
    print("2.Sub(-)")
    print("3.Mul(*)")
    print("4.Div(/)")
    print("5.Mdiv(%)")
    while True:
        #take input from the user.
        choice = input("Enter the calculation operation(1 / 2 / 3 / 4 / 5) :")
        #check if the input is one of the four options
        if choice in ['1','2','3','4','5']:

            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
            if choice=='1':
                print(f"Addition of {num1} + {num2} is = {Addition(num1,num2)}")
            
            if choice=='2':
                print(f"Subtraction of {num1} - {num2} is = {Subtraction(num1,num2)}")
            
            if choice=='3':
                print(f"Multiplication of {num1} * {num2} = {Multiplication(num1,num2)}")
            
            if choice=='4':
                print(f"Division of {num1} / {num2} is = {Division(num1,num2)}")
            
            if choice=='5':
                print(f"Modulo division of {num1} % {num2} is  = {ModuloDivision(num1,num2)}")

        next_calculation=input("Do you want to perform another calculation (Yes / no ):")
        if next_calculation.lower() != "yes":
            break 
    print("Bye calculator Take care see you later!**")
CALUCLATOR()




