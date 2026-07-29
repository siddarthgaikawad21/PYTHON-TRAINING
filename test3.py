# Raiseing Error 
try:
    num=int(input("Enter the value of Mark : "))
    if num>100:
        raise ValueError("Mark cannot be greater than 100")
        print("Total mark :",num) 
except ValueError as e:
    print("Error:",e)        