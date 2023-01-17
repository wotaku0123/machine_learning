largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        if largest is None:
            largest = int(num)
        elif largest < int(num):
            largest = int(num)
        elif smallest is None:
            smallest = int(num)
        elif smallest > int(num):
            smallest = int(num)
    except:
        print('Invalid input')
        continue
    

print("Maximum is", largest)
print("Minimum is ", smallest)