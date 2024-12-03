import random

# Generate a random integer between 1 and 10 (inclusive)
name=input("Enter Your Name ")
print("Nice to meet you:",name)
print("Let us Then Start the Game \n The Questions will be based on Indian History")

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
       case 2:
        print("The territory of Porus who offered strong resistance to Alexander was situated between the rivers of")
        print(" 1. Sutlej and Beas \n 2. Jhelum and Chenab \n 3. Ravi and Chenab \n 4. Ganga and Yamuna")
        k= int(input("Enter The Correct Option "))
        match k:
          case 1:
           print("You Have Entered the wrong Answer\n The Correct Answer is Jhelum and Chenab")
          case 2:
            print("You Have Entered the correct Answer")
          case 3:
            print("You Have Entered the wrong Answer\n The Correct Answer is Jhelum and Chenab")
          case 4:
            print("You Have Entered the wrong Answer\n The Correct Answer is Jhelum and Chenab")
       case 3:
        print("Under Akbar, the Mir Bakshi was required to look after")
        print(" 1. military affairs \n 2. the state treasury \n 3. the royal household \n 4. the land revenue system") 
        k= int(input("Enter The Correct Option "))
        match k:
          case 1: 
             print("You Have Entered the correct Answer")
          case 2:
             print("You Have Entered the wrong Answer\n the Correct Answer is  military affairs")
          case 3:
             print("You Have Entered the wrong Answer\n the Correct Answer is  military affairs")
          case 4:
             print("You Have Entered the wrong Answer\n the Correct Answer is  military affairs")
       case 4:
        print("Tripitakas are sacred books of")
        print("1. Buddhists \n 2. Hindus \n 3. Jains \n 4. None of the Above")
        k= int(input("Enter The Correct Option "))
        match k:
          case 1: 
             print("You Have Entered the correct Answer")
          case 2:
             print("You Have Entered the wrong Answer\n the Correct Answer is Buddhists")
          case 3:
             print("You Have Entered the wrong Answer\n the Correct Answer is Buddhists")
          case 4:
             print("You Have Entered the wrong Answer\n the Correct Answer is Buddhists")
       case 5:
         print("The trident-shaped symbol of Buddhism does not represent")
         print("1. Nirvana \n 2. Sangha \n 3. Buddha \n 4. Dhamma")
         k= int(input("Enter The Correct Option "))
         match k:
          case 1: 
             print("You Have Entered the correct Answer")
          case 2:
             print("You Have Entered the wrong Answer\n the Correct Answer is Nirvana ")
          case 3:
             print("You Have Entered the wrong Answer\n the Correct Answer is Nirvana ")
          case 4:
              print("You Have Entered the wrong Answer\n the Correct Answer is Nirvana ")
       case 5:
        print("The theory of economic drain of India during British imperialism was propounded by")
        print("1. Jawaharlal Nehru \n 2. Dadabhai Naoroji \n 3. R.C. Dutt \n 4. M.K. Gandhi")
        k= int(input("Enter The Correct Option "))
        match k:
          case 1:
           print("You Have Entered the wrong Answer\n The Correct Answer is Dadabhai Naroji")
          case 2:
            print("You Have Entered the correct Answer")
          case 3:
            print("You Have Entered the wrong Answer\n The Correct Answer is Dadabhai Naroji")
          case 4:
            print("You Have Entered the wrong Answer\n The Correct Answer is Dadabhai Naroji") 
       case 6:  
        print("The treaty of Srirangapatna was signed between Tipu Sultan and")
        print("1. Robert Clive \n 2. Cornwallis \n 3. Dalhousie \n 4. Warren Hastings")
        k= int(input("Enter The Correct Option "))
        match k:
          case 1:
           print("You Have Entered the wrong Answer\n The Correct Answer is Cornwallis")
          case 2:
            print("You Have Entered the correct Answer")
          case 3:
            print("You Have Entered the wrong Answer\n The Correct Answer is Cornwallis")
          case 4:
            print("You Have Entered the wrong Answer\n The Correct Answer is Cornwallis") 
       case 7:
        print("The system of competitive examination for civil service was accepted in principle in the year")         
        print("1. 1833 \n 2. 1853 \n 3. 1858 \n 4. 1882")
        k= int(input("Enter The Correct Option "))
        match k:
          case 1:
           print("You Have Entered the wrong Answer\n The Correct Answer is 1853")
          case 2:
            print("You Have Entered the correct Answer")
          case 3:
            print("You Have Entered the wrong Answer\n The Correct Answer is 1853")
          case 4:
            print("You Have Entered the wrong Answer\n The Correct Answer is 1853")



      





 


                 
for i in range(1,18):
  #  n = random.randint(1, 10)
  n= int(input("Enter The Correct Option "))
  Question(n)
     
     