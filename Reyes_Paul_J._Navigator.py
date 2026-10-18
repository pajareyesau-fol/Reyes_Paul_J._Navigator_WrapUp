print("TRAVEL EXPENSES")

name = input("Enter your name: ")
destination = input("Enter destination: ")

transportation = float(input("Transportation: "))
hotel = float(input("Hotel: "))
food = float(input("Food: "))
other = float(input("Other expenses: "))
budget = float(input("Your budget: "))

total = transportation + hotel + food + other
remaining = budget - total

print("Name:", name)
print("Destination:", destination)
print("Total Expenses:", total)
print("Budget:", budget)
print("Remaining Money:", remaining)

if total <= budget:
    print("You are within your budget!")
else:
    print("You exceeded your budget!")
