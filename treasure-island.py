#100DaysOfCode #AppBrewery #Python

print('''
# insert ASCII art here
''')

print("Welcome to Misinformation Island!")
print("Your mission is to find the truth--or to get as close to it as you can.\n") 

wmd = input("Were you convinced that Iraq had WMDs in 2003? [right]\n")
wmd = wmd.lower()
if wmd == "right":
	print("Game Over. Get back to us when those WMDs turn up.\n")
else:
	guns = input("Were you convinced that Barack Obama was on the verge of confiscating guns and imprisoning gun owners in concentration camps? [fire or safety on]\n")
	if guns.lower() == "fire":
		print("Game Over. Alex Jones is entertaining but always DYOR.\n")
	else:
		infowars = input("Are you convinced that Sandy Hook was a false flag operation? [yes or no]\n")

		if infowars.lower() == "yes":
			print("Game Over. Wow! You're a hardcore InfoWars fan.\n")
		else:
			source = input("Which of these news sources do you trust the most? [red for InfoWars; ue for CNN; yellow for 'I always maintain healty scepticism.']\n")
			if source.lower() == "red":
				print("Game Over. Always DYOR!\n")
			elif source.lower() == "blue":
				print("Game Over. CNN tries hard but always DYOR.\n")
			elif source.lower() == "yellow":
				print("You're awesome for not shunning sources that disagree with your world view! Keep up the good work!\n")

