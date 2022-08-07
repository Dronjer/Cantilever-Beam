# Calculating for any cantilever beam with width (b) and height (h) and length (l)
# Calculating the moment of inertia for the cantilever beam
# this code is for solid beam with width, height and length 
print("enter the width of the beam")
b = float(input())
print("enter the height of the beam")
h = float(input())
I = (b*(h**3))/12
y = h/2
print("the moment of inertia of the given beam is", I)
# P is the load
print("If you have specific values for the load and length then press Y or else N")
# If you have specific value of load and length
User_input = input()
if User_input == "Y":
    print("Enter the value of load")
    F = float(input())
    print("Enter the length")
    l = float(input())
    m = F*l
    Bending_Stress = m*y/I
    print("For the entered value of F and l, the bending stress value is", Bending_Stress)
elif User_input == "N":
    # The load is given as in the problem.
    P = (5000, 10000, 15000, 20000, 25000, 30000)
    for j in P:
        k = (0.25, 0.5, 0.75, 1)
        for i in k:
            M = i * j
            print("The bending moment for the given loads and length", M)
            # Calculating the bending stress for the different loads and length
            S = M * y / I
            print("The value of bending stress for the given stress and load is", S)