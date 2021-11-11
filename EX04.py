# Shubham EX04
import pandas

file = open("citi_bike.txt", "r")  # open citi bike text file for reading
data = []  # create empty list

for line in file:  # read each line
    parts = line.strip().split()  # strip the white space and create list of items
    data.append(parts)  # append that line’s items list to the data list


def details(data):
    average_daily_miles = 0
    total_24hrpasses_purchased = 0
    top5_dict = {}
    index = 0
    for x in data:
        average_daily_miles += float(x[3])
        total_24hrpasses_purchased += float(x[7])
        top5_dict[index] = float(x[1])
        index += 1
    top5list = sorted(top5_dict, key=top5_dict.get, reverse=True)[:5]
    average_daily_miles = average_daily_miles / len(data)
    print()
    print("The following data is from {} to {}:".format(data[0][0], data[-1][0]))
    print()
    print("Average Miles: {}".format(average_daily_miles))
    print("Total number of passes purchased: {}".format(total_24hrpasses_purchased))
    print("Top 5 days with higher number of trips: ")
    for x in top5list:
        print(data[x])
    print()


details(data)

# CSV File Processing
file2 = open("citi_bike.csv", "r")
data2 = []
for line in file2:
    parts = line.strip().split(",")
    data2.append(parts)
details(data2)
print()
df1 = pandas.DataFrame(data)
df2 = pandas.DataFrame(data2)
df_full = pandas.concat([df1, df2])
print(df_full)

print()
print("This is the end of the files processing.")
