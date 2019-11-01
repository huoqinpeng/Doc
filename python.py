# number = int(input("Enter an integer:"))
# if number <= 100:
#     print("your number is less then or equal to 100")
# else:
#     print("your number is greater then 100")

amount = float(input("Enter amount:"))
inrate = float(input("Enter Interest rate:"))
period = int(input("Enter period:"))
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs.{:.2f}".format(year,value))
    amount = value
    year = year +1
