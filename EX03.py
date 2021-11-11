# Shubham EX03
# Part 1
Jan_Feb = open("NYC-CitiBike-Jan_Feb2016.csv", 'r')
n0 = 0
n1 = 0
n2 = 0
print("\nThe following are the first 5 lines of the Jan_Feb2016.csv file:")
print("")
for row in Jan_Feb:
    if n0 < 5:
        print(' ', row)
    if 'Subscriber' in row:
        n2 += 1
    if 'Customer' in row:
        n1 += 1
    n0 += 1
z1 = (n2 / n0) * 100
print("The file has", n0, "lines,", n1, "of them have Customer as usertype"
      , n2, "of them have Subscriber as usertype.",
      "\nSubscribers are", z1, "% of the total")

# Part 2
Apr_May = open("NYC-CitiBike-Apr_May2016.csv", 'r')
n3 = 0
n4 = 0
n5 = 0
print("\nThe following are the first 5 lines of the Apr_May2016.csv file:")
print("")
for row in Apr_May:
    if n3 < 5:
        print(' ', row)
    if 'Subscriber' in row:
        n5 += 1
    if 'Customer' in row:
        n4 += 1
    n3 += 1
z2 = (n5/n3)*100
print("The file has", n3, "lines,", n4, "of them have Customer as usertype"
      , n5, "of them have Subscriber as usertype.",
      "\nSubscribers are", z2, "% of the total")
if n0 > n3:
    print ('\nThe first file is larger than the second\n')
else:
    print('\nThe first file is smaller than the second\n')
if z1 > z2:
    print ('The percentage of Subscriber in the first file is larger than in the second one\n')
else:
    print('The percentage of Subscriber in the first file is smaller than in the second one\n')
