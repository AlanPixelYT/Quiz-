import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


print(f"{Fore.BLUE} Welcome to Alan's amazing awesome adventure! \n")

print(f"{Fore.BLUE}W{Fore.RED}E{Fore.GREEN}L{Fore.MAGENTA}C{Fore.YELLOW}O{Fore.CYAN}M{Fore.RED}E")

score = 0
input(f"{Fore.RED}Press Enter to continue...")

print (f"{Fore.WHITE} Okay! So, what we will be doing is there will be a quiz! I will be asking you a lot of \n questions about me, my life and really everything about me in general! ")

print (" Okay! Let's start!")

input("Press Enter to start!")

question1 = input (" \n How old is Alan?")

if question1 == "12":
  print("correct!")
  score = score + 1


elif question1 == " 12":
  print("correct!")
  score = score + 1

elif question1 == " twelve":
  print("correct!") 
  score = score + 1

else: 
  print("incorrect! Alan is twelve years old!") 
  score = score - 1

print ("Your score is", + score)

