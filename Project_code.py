import random
import time
possible_rolls = [5, 7, "$"]




def chance(a,b,c):   

   balance = 100
   num_of_spins = int(input("\nStarting balance: 100\n Cost per spin: 10\n How many times would you like to spin?: "))

   while num_of_spins > 0 and balance >= 10:

      num_of_spins -= 1

      if a == "$" and b == "$" and c == "$":
         balance += 210
         print("\nGrand jackpot\n +210 balance\n Current balance:", balance)
      
      elif a == 7 and b == 7 and c == 7:
         balance += 70
         print("\nJackpot\n +70 balance\n Current balance:", balance)
      elif a == 5 and b == 5 and c == 5:
         balance += 70
         print("\nJackpot\n +70 balance\n Current balance:", balance)
      else:
         balance -= 10
         print("\nCurrent balance:", balance)
      
      print("\n(",a,b,c,")\n")
      time.sleep(1)

      a = random.choice(possible_rolls)
      b = random.choice(possible_rolls)
      c = random.choice(possible_rolls)

      if num_of_spins == 0 and balance >= 10:         #only runs on last spin
         continue_ = input("\nWould you like to keep spinning? (Y) or (N): ")


      if num_of_spins == 0 and balance >= 10 and continue_ == "Y":     #only runs on last spin
         num_of_spins = int(input("\nHow many times would you like to spin?: "))
       
   if balance < 10:
      print("Not enough balance, better luck next time")

   
   return "Final balance:", balance

      






product = chance(random.choice(possible_rolls),random.choice(possible_rolls),random.choice(possible_rolls))




print(product)
