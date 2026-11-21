while True:
    try:
        name = input("Enter your name: ")
        print("Hello ",name)
    except Exception as e:
        print(e)
    break
print("Let's perform some basic operation")
print("'+' for addition.")
print("'-' for subtraction.")
print("'*' for multiplication.")
print("'/' for division.")
print("'%' for remender.")

def operation():
    num1=float(input("Enter the first number= "))
    num2=float(input("Enter the another number= "))
    op=input("Enter the operation to do: ") 
    if op=="+":
        print(num1+num2)
    elif op=="-":
        print(num1-num2)
    elif op=="*":
        print(num1*num2)
    elif op=="/":
        try:
            result=num1/num2
        except ZeroDivisionError:
            print("Denominator can't be zero.")
        else:
            print(num1/num2) 
    elif op=="%":
        print(num1%num2)
    else:
        print("You enter the inappropriate operation.")

operation()
        
while True:    
    more=input("Do you want to perform more peration(Y/N): ")
    if more=="Y":
        operation()
    elif more=="N":
        break
    else:
        print("You enter the wrong input.")
print("Thank you ",name)
    



