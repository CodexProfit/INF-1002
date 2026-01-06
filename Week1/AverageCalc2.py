
a = input("insert first number: ")
b = input("insert second number: ")
c = input("insert third number: ")

try:
    a = float(a)
    b = float(b)
    c = float(c)

    average = (a + b + c) / 3
    print("Your average is:%0.2f" % average)

except:
    print("Your input is invalid!")