import random
import time

description = '''\n########## Carrot in the box instructions ##########

This is a bluffing game where you and your opponent tries to select the box with the carrot inside of it.
Only one box has a carrot inside of it. To win, you must choose the box with the carrot inside of it. 

This is a simple game of persuasion and betrayal.

- Player one looks in their box whilst the opponent closes their eyes.
- Player one then says that their box has/hasn't got the carrot inside. (Player 1 can choose either)
- Player two then decides to swap or keep the boxes.

########## Carrot in a box instructions ##########
'''

print(description)

input("Please push enter... ")

P1 = input("Hooman 1, Enter your name: ")
P2 = input("Hooman 2, Enter your name: ")

title = P1.center(11) + '   ' + P2.center(11)

print()
print(title)
print()
print(f"{P1}, You have a RED box in front of you")
print(f"{P2} You have a BLU box in front of you")
print()
print(f"{P1} Look in the box.")
print(f"{P2} Look away.")
print()

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print(f"{P1}, lets open up the box!")

if random.randint(0, 1) == 1:
    CIFB = True
else:
    CIFB = False

if CIFB:
    print()
    print('                     🥕 \n'
'(YOUR BOX) RED Box > 📦')
    print()
else:
    print()
    print('                      🥕 \n'
'(NOT YOURS) BLU Box > 📦')
    print()

input('Please push enter... ')

print("\n"*100)
print("Don't think that i'm THAT stupid? Of course I hid it.")
print(f"{P1}, Now, Choose your response")
print("1.} There is a carrot ")
print("2.} There is no carrot ")
print()
input("Please push enter... ")

print()
print(f"{P2}, wanna swap?")
while True:
    response = input('Y/N > ').upper()
    if not (response.startswith("Y") or response.startswith("N")):
        print(f"{P2}, please enter Yes or No")
    else:
        break

fb = 'RED'
sb = "BLU"

if response.startswith("Y"):
    CIFB = not CIFB
    fb, sb = sb, fb
    print()
    print("swapped")
    print()
    print()
else:
    print()
    print("Not swapped")
    print()
    print()

input("Please push enter... ")
print()
print("HERE ARE THE RESULTS")
print()
print("Drumroll please...")
time.sleep(3)
if CIFB:
    print(f'''{P1}'s Box > 📦''')
else:
    print(f'''{P2}'s Box > 📦''')

if CIFB:
    print(f"{P1} WON!!!")
else:
    print(f"{P2} WON!!!")