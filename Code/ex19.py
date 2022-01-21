# Define function cheese_and_crackers with two arguments cheese_count and
# boxes_of_crackers and print the values.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
# Here we pass values to function directly
cheese_and_crackers(20, 30)

print("OR, we can use variables from our scripts:")
amount_of_cheese = 10
amount_of_crackers = 50
# Here we pass value to function via variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# Here we do calculation to pass to function.
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
