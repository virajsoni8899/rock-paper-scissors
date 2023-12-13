import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
image_lsit = [rock,paper,scissors]
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >=3 or user_choice < 0:
   print("invalid number you lose")
else:
  
  print(image_lsit[user_choice])
  print("you choose")
  computer_choice = random.randint(0,2)
  print(image_lsit[computer_choice])
  print("computer choose") 
if user_choice == 0 and computer_choice ==2:
  print("you win!")
elif user_choice == 0 and computer_choice ==1:
  print("you lose")
elif user_choice == 1 and computer_choice ==0:
  print("you win!")
elif user_choice == 1 and computer_choice ==2:
  print("you lose")
elif user_choice == 2 and computer_choice ==0:
  print("you lose")
elif user_choice == 2 and computer_choice ==1:
  print("you win!")
else:
  print("it's a tie")
  


