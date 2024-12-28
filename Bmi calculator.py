weight = float(input("Enter Your Weight in Kg: "))
height = float(input("Enter Your Height in Meter: "))

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}")

if bmi <=18.4:
    print("You are underweight.")

elif bmi <=24.9:
    print("You are healthy.")    
    
elif bmi <=29.9:
    print("You are over weight.")    
    
elif bmi <=34.9:
    print("You are severely over weight.")    
    
elif bmi <=39.9:
    print("You are obese.")    
    
else:
    print("You are severeky obese.")    