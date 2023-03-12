print("Favourite Christmas Movie Quiz!")
print()
movie = input("What is your favourite Christmas movie?")
print()
if movie == "elf" or "Elf":
  print("Really? Elf is the best!")
  print()
  faveCharacter = input("Who is your favourite character?")
  print()
  if faveCharacter == "Buddy" or "buddy":
    print("Yup, Buddy's the most hilarious Christmas movie character ever!")
  else:
    print("That character is okay, I guess...")
elif movie == "How the grinch stole christmas" or "how the grinch stole christmas" or "How The Grinch Stole Christmas" or "How the Grinch stole Christmas":
  print("The absolute greatest Christmas movie ever created!")
  print()
  movieVersion = input("Do you prefer the live action, or the new cartoon version?")
  print()
  if movieVersion == "Live Action" or "live action" or "Live action":
    print("Live Action TV is awesome, especially when you're watching the Grinch!")
  else:
     print("That's great and all...")
else:
  print("Well, everyone's got their own tastes in movies..")  