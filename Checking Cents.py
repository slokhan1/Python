# Shubham EX02
while True:
    cents = input("Enter price in cents or a multiple of 5 cents or 'done' if finished:")
    if cents == "done":
        print("Good Bye!")
        break
    else:
        if cents.isalpha() == True:
            print("Wrong Input.",cents,"is not numerical!")
        elif float(cents)<0 :
            print("Invalid price",cents,"is a negative value")
        elif int(cents) > 1000 :
            print("Invalid price",cents,"is not below 1000")
        elif int(cents)%5 != 0:
            print("Invalid price",cents,"is not a multiple of 5")
        else:
            print("You entered",cents,"cents")
        continue
