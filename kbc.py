import random

# Generate a random integer between 1 and 17 (inclusive)
name=input("Enter Your Name ")
print("Nice to meet you:",name)
print("Let us Then Start the Game")

def Question(a):
    match a:
       case 1:
         print("The Battle of Plassey was fought in")
         print(" 1. 1757 \n 2. 1748 \n 3. 1782 \n 4. 1764")
         k= int(input("Enter The Correct Option "))
         match k:
          case 1: 
            print("You Have Entered the correct Answer")
          case 2:
            print("You Have Entered the wrong Answer\n The Correct Answer is 1757")
          case 3:
            print("You Have Entered the wrong Answer\n The Correct Answer is 1757")
          case 4:
            print("You Have Entered the wrong Answer\n The Correct Answer is 1757")    
for i in range(1,18):
    random_integer = random.randint(1, 17)


    Question(n)
     
     