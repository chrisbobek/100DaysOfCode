# Don't change the code below
print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

# Write your code below this line

true_total = 0
love_total = 0

# List of strings
names = [name1.lower(), name2.lower()]

# 'true' and 'love' strings converted to lists
true_list = list("true")
love_list = list("love")

for name in names:
    for letter in true_list:
        true_total += name.count(letter)
    for letter in love_list:
        love_total += name.count(letter)


# Concatenate the string versions of the digits
strScore = f"{true_total}{love_total}"

# Convert string score to int
intScore = int(strScore)

# Determine score
if (intScore < 10) or (intScore > 90):
    print(f"Your score is {intScore}, you go together like coke and mentos.")
elif (intScore >= 40) and (intScore <= 50):
    print(f"Your score is {intScore}, you are alright together.")
else:
    print(f"Your score is {intScore}.")


