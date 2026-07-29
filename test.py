try:
    a=10
    b="0"
    print("Division",a/b)
except ZeroDivisionError:
    print("Cant divide with Zero")
except TypeError:
    print("Enter the integer Value")
else:
    print("Program Run successfully") 
finally:
    print("Mujhe kuch nhii pata saale")       
    