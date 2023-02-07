#TTA
#number guess 1 to 50
#Matt Green
#10/08/22


import random
print ("Hello and welcome try to guess a number between 1-50")
myName = input("Hello !What is your name ?")
number = random.randint (1,50)
print (number)
print ("Well,"+myName+"I am thinking of a number between 1 and 50.")
guess =int(input ("Take a guess:")  )
if guess== number:
  print ("Well done "+ myName +"You guessed my number")
else:
  print("Wrong ,better luck next time")
        
  




































