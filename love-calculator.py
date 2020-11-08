# Don't change the code below
print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

# Write your code below this line

true_total = 0
love_total = 0

# List of strings
names = [name1, name2]

# 'true' and 'love' strings converted to lists
true_list = list("true")
love_list = list("love")

for name in names:
    for letter in true_list:
        true_total += name.count(letter)
    for lettter in love_list:
        love_total += name.count(letter)

print(f"true: {true_total}")
print(f"love: {love_total}")

