# Shubham Ex01
while True:
    x = input("How many US Dollars do you want to exchange?\n'example:100'\nType value or 'done' to exit:")
    if x =='done':
        print('\nThanks for using Python')
        break
    if x.isdigit() == False:
            continue
    print("The input is $",x)
    y=input("Enter the name of the currency you are converting dollars to\n'example:INR':")
    print("Currency type is",y)
    break
while True:
    if x =='done':
        break
    z=input("What is the exchange rate?:\n'example:74':")
    if z.isdigit() == False:
        continue
    else:
        print("The exchange rate is", z)
        n=int(x)*int(z)
    print()
    print("You can exchange",x,"US dollars for",n,"INR")
    break
