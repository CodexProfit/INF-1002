print("Insert your preferred unit here")
print("1. Metric")
print("2. Imperial")

while True:
    a = input("Please select your unit (metric/imperial): ")
    if a.lower() in ["metric", "imperial"]:
        break
    else:
        print("Invalid unit. Please enter 'metric' or 'imperial'.")

b = input("What is your height? ")
c = input("What is your weight? ")

try:
    b = float(b)
    c = float(c)
except:
    print("Your input is invalid!")
    exit()
    
if a == "metric":
    BMI = c / (b ** 2)
else:
    BMI = 703 * c / (b ** 2)

if BMI <= 16:
    category = "Severe Thinness"
elif BMI <= 17:
    category = "Moderate Thinness"
elif BMI <= 18.5:
    category = "Mild Thinness"
elif BMI <= 25:
    category = "Normal"
elif BMI <= 30:
    category = "Overweight"
elif BMI <= 35:
    category = "Obese Class I"
elif BMI <= 40:
    category = "Obese Class II"
else:
    category = "Obese Class III"
print("%0.2f %s" % (BMI, category))

