print("Positivity Generator")
print()
name = input("Name: ")
print()
weather = input("What is the weather like today?: ")
print()
time = input("Is it morning, afternoon or evening?: ")
print()
feeling = input("How are you feeling today on a scale of 1 to 10?: ")
print()
print("So, your name is",name,", you are currently feeling",feeling,",on a scale of 1-10, and the weather is", weather,"?")
confirm = input( )
if confirm == "yes" or confirm == "Yes":
  print()
  if feeling == "1" or feeling == "2" or feeling == "3":
    print("Aww, cheer up,",name,"although you're probably feeling terrible at the moment, there's nowhere left to go now but up. 🙂")
  if feeling == "4" or feeling == "5" or feeling == "6": 
    print("Sounds like you've been having a pretty good day! Remember to enjoy the good things in life!")
  if feeling == "7" or feeling == "8" or feeling == "9" or feeling == "10":
    print("Wow! You are looking amazing today! Remember to always keep up the positivity!")
else:
 print("I'm sorry, I don't know your name, but my goodness do you look simply stunning today!")