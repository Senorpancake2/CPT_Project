import random
list = [5, 7, "$"]
balance = 100
continue_ = input("Starting balance: 100\n Would you like to take your chances?: ")

def chance(a,b,c):

   if balance == 0:


      if a == "$" and b == "$" and c == "$":
         balance += 10000
         print("Grand jackpot\n Current balance:", balance)
      
      elif a == 7 and b == 7 and c == 7:
         balance += 1000
         print("Jackpot\n Current balance:", balance)
      elif a == 5 and b == 5 and c == 5:
         balance += 1000
         print("Jackpot\n Current balance:", balance)
      else:
         balance -= 10
   
      return a,b,c











product = chance(random.choice(list),random.choice(list),random.choice(list))

print(product)
