# Don't change the code below
print("Welcome to Python Pizza Delivery!")

size = input("Which size pizza do you want? S, M, or L ")

add_pepperoni = input("Do you want pepperoni? Y or N ")

extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above

# Write your code below this line

# Size
small = 15
medium = 20
large = 25

# Pepperoni
pepperoni_small = 2
pepperoni = 3

# Cheese
add_cheese = 1

total = 0

if size == 'S':
    total = small
elif size == 'M':
    total = medium
else:
    total = large

if add_pepperoni == 'Y':
    if size == 'S':
        total += pepperoni_small
    else:
        total += pepperoni

if extra_cheese:
    total += add_cheese

print(f"Your final bill is: ${total}")


