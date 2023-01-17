count = 0
sum = 0
print('Before', count, sum)
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + thing
    print(count, count, thing)

print('After', sum, sum / count)

smallest = None

print('Before')

for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)

print('After', smallest)

#  'is' is for True, false, None
