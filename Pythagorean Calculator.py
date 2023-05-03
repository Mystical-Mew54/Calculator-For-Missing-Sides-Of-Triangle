#Pythagorean Calculator
import math

#This is the function for how to solve for a missing hypotenuse
def missing_hyp(leg1, leg2):
    #This gives simple equation of C^2 = A^2 + B^2
    hyp = (leg1**2) + (leg2**2)
    
    #This calls for the square root of C^2
    c = math.sqrt(hyp)
    return c
    
    
#This is the function for how to solve for a missing side
def missing_side(leg, hyp):
    #This is the equation of B^2 = C^2 - A^2
    miss_leg = (hyp**2) - (leg**2)
    
    #This finds the square root of B^2
    leg = math.sqrt(miss_leg)
    return leg
    
    
#This asks the user for what they need to find
decision = int(input("Need to find hypotenuse[1] or a side[2]? "))


#This calls the function on how to solve for a missing hypotenuse
#and asks for the relevant information
if decision == 1:
    leg1 = int(input("Side 1: "))
    leg2 = int(input("Side 2: "))
    print("-----------")
    print("Hypotenuse: " + str(missing_hyp(leg1, leg2)))


#This calls the function on how to solve for a missing side and
#asks for the relevant info
else:
    leg = int(input("Side: "))
    hyp = int(input("Hypotenuse: "))
    print("-----------")
    print("Missing Side: " + str(missing_side(leg, hyp)))
