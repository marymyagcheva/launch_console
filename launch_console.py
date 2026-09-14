print("Welcome to the Launch Console!")


name = 'Mariya'
print("hi", name)
menu  = ["About me", "My goals", "Exit"]
def about_me(name):
print("My name is Mariya.")

choice = "3"

if choice == "3":
          print("Goodbye!")
elif choice > "3":
          print("try less")
else:
          print("try more")


running = True
while running == True:
    print("running")
    break          


def mystery(words):
    out = ""
    for w in words:
        out = out + w[0]
    return out
print(mystery(["Grit", "Impact", "Trust"])) 

choice = "3"
running = True
if choice == "3":
    print("Goodbye!")
    running = False
else:
    print("Please pick a valid option.")
