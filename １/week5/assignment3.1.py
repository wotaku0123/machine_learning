hrs = input("Enter Hours:")
rate = input("Enter Hourly Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Enter the integer")
    quit()

sum = h * r

if h > 40:
       sum = (40 * r) + ( h - 40) * r * 1.5;

print(sum)