import random


while True:

  uch  = input("\n Enter either rock, paper, or scissors: ")



  lst = ["rock","paper","scissors"]


  random.shuffle(lst)

  comp_choice = (lst[0])


# uch loses

  if comp_choice == "rock" and uch == "scissors":
    print(f"Computer chose Rock. Rock destroys scissors, you lose!\n")

  elif comp_choice == "scissors" and uch == "paper":
    print(f"Computer chose Scissors. Scissors cut paper, you lose!\n")

  elif comp_choice == "paper" and uch == "rock":
    print(f"Computer chose Paper. Paper covers rock, you lose!\n")

#uch wins

  elif comp_choice == "rock" and uch == "paper":
    print(f"Computer chose Rock. Rock gets covered by paper, you win!\n ")

  elif comp_choice == "scissors" and uch == "rock":
    print(f"Computer chose Scissors. Scissors get destroyed by rock, you win!\n ")

  elif comp_choice == "paper" and uch == "scissors":
    print(f"Computer chose Paper. Paper is destroyed by scissors, you win!\n ")

# uch ties

  elif comp_choice == uch:
    print(f"You both chose {uch}, it's a tie!\n ")


  elif uch != "paper" or "scissors" or "rock":
    print("Nice try. Enter a valid input.")
    continue

  restart = str(input("Press Enter to play again "))

  if restart == "":
    continue
  
    