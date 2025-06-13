def add(x,y):
    return x+y
def subract(x,y):
    return x-y
def multiple(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return"Error! Division by zero is not allowed."
    else:
        return x/y
def calulator():
    print("Basic Calculator")
    print("1. Addition")
    print("2. Subraction")
    print("3. Multiplication")
    print("4. Division")

    choice=input("Enter your choice (1/2/3/4):")

    if choice in ['1','2','3','4']:
       num1=float(input("Enter First number:"))
       num2=float(input("Enter Second number:"))

       if choice=='1':
           print(f"{num1}+{num2}={add(num1,num2)}")
       elif choice=='2':
           print(f"{num1}-{num2}={subraact(num1,num2)}")
       elif choice=='3':
           print(f"{num1}*{num2}={multiple(num1,num2)}")
       else:
           print(f"{num1}/{num2}={division(num1,num2)}")
    else:
        print("Invalid choice.")
if __name__=="__main__":
    calulator()
