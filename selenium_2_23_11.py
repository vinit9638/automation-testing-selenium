# b = 10 

try:
    a = int(input("ENter number 1:- "))
    b = int(input("ENter number 2:- "))
    print(a / b)

except ZeroDivisionError:
    print("Number cant be divide by ZERO")

except Exception as e:
    
    print("Sorry we cant process your data...")
    print("This is the reason >> ",e)

finally:
    print("Hello1")


print("Your COde is working fine")
print("End of code")