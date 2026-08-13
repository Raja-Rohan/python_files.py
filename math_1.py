import math

q1= int(input("""
Convert the following formulas in algebraic notation to Python computer notation. 

1)  y=3x+5				y = 3 * x + 5

2)  a=(v-u)/t				a = (v - u) / t

3)  F=(mv^2)/r				F = (m * v **2) / r


Just enter the question number: """))

if q1 == 1:

    x = int(input("Enter the value of x: "))
    y = 3 * x + 5
    print(f"Y = {y}")

elif q1 == 2:

    v = int(input("Enter value of v: "))
    u = int(input("Enter value of u: "))
    t = int(input("Enter value of t: "))
    a = (v - u) / t
    print(f"Value of a ={a}")

elif q1 == 3:
    m = int(input("Enter value of m: "))
    v = int(input("Enter value of v: "))
    r = int(input("Enter value of r: "))
    f = (m * v **2) / r
    print(f"Value of f ={f}")

else:
    print("Enter a valid number!")
