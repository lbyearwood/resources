import turtle
import random
import sys

t = turtle.Turtle()
turpos = 0
def wrongone():
   t.backward(300)
   t.right(90)
   t.pendown()
   t.backward(250)
   print("One wrong")

def wrongtwo():
   t.right(90)
   t.backward(150);print("2 wrong")

def wrongthree():
   t.right(90)
   t.backward(50);print("three wrong")

def wrongfour():
   t.penup()
   t.left(90)
   t.pendown()
   r = 20
   t.circle(r);print("Four wrong")

def wrongfive():
   t.left(90)
   t.penup()
   t.forward(40)
   t.pendown()
   t.forward(100);print("Five wrong")


def wrongsix():
   t.left(45)
   t.forward(50)
   t.goto(-150.00,60.00);print("Six wrong")

def wrongseven():
   t.right(90)
   t.forward(50)
   t.goto(-150.00,60.00);print("Seven wrong")

def wrongeight():
   t.left(45)
   t.backward(60)
   t.right(90)
   t.forward(60)
   print("8 wrong")

def wrongnine():
   t.backward(120)
   print("9 wrong")


words = ["haram","movie","charismatic","intervene","broadcast","bald","professional","invite","apathy","education"]
wordn = random.randint(0,len(words)-1)
word = words[wordn]
wordlist = list(word)
mistakes = 0
invisiblelist = []
for i in range(0,len(wordlist)):
   invisiblelist.append("_")
asda = 0
correct = False
while True:
   asda = 0
   print(invisiblelist)
   ask = input("Input a letter\n")
   for i in range(0,len(wordlist)):
      if wordlist[i] == ask:
           print(ask)
           wordlist[i] = " "
           invisiblelist[i] = ask
           #ok = list(word)
           #z = ok.pop(i)
           #print(z);print(ok)
           #word = "".join(ok)
           #print(word)
           asda = 0
           correct = True
           break
      else:
           asda += 1
           correct = False

   if asda >= len(word)-1:
       mistakes = mistakes + 1
   if mistakes == 1 and correct == False:
       wrongone()
   elif mistakes == 2 and correct == False:
       wrongtwo()
   elif mistakes == 3 and correct == False:
       wrongthree()
   elif mistakes == 4 and correct == False:
       wrongfour()
   elif mistakes == 5 and correct == False:
       wrongfive()
   elif mistakes == 6 and correct == False:
       wrongsix()
   elif mistakes == 7 and correct == False:
       wrongseven()
   elif mistakes == 8 and correct == False:
       wrongeight()
   elif mistakes == 9 and correct == False:
       wrongnine()
       sad = input(f"Click enter to finish the program, you failed...the word was {word}")
       sys.exit()
   if "".join(invisiblelist) == word:
       print("Correct word","".join(invisiblelist))
       break
   else:
       pass


sam = input("Enter to finish the program")