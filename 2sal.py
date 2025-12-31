basic_pay = float(input("enter basic pay : "))
hra = 0.10 * basic_pay
ta= 0.05 * basic_pay

gross= hra + ta + basic_pay

tax = 0.02 * gross

total_sal = gross-tax
print("gross sal  = ",  gross)
print("net salary = ", total_sal)

# same type questions :
 # percentage
total=0
for i in range (5):
    marks= float( input ( " enter marks : "))
    total += marks
percentage= (total /500 ) * 100
print(" percentage = ",percentage)

# Temperature Conversion

c = float(input("Enter temperature in Celsius: "))

f = (c * 9/5) + 32
print("Temperature in Fahrenheit =", f)