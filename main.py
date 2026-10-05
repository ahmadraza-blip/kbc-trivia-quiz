""" Program displaying questions to user like KBC.
Use list data type to store the question and their correct answers.
Display the final amount the person is taking home after playing the game"""
user=input("Enter a name:")
instructions=["WELCOME IN SHOW(KBC)" ,
              "YOU GIVE ONLY 4 ANSWERS OF QUESTIONS" ,
               "TOTAL AMOUNT OF THIS GAME=$10000" ,
               "IF YOU GIVE ONE WRONG ANSWER GAME WILL BE STOP."]
for instruction in instructions:
     print(instruction)
user=input("ARE YOU READY FOR FIRST QUESTION(Yes/No):")
if user=="Yes":
    print("YOUR FIRST QUESTION TOTAL AMOUNT=$1000")
    Question=[
         "Who is the founder of Pakistan?" ,
         "1"
         ]
    print(Question[0])
elif user=="No":
    print("Okay!I understand take a time.")
    user=input("After 10sec To access Question (Ready) [otherwise you loss this game] Type Ready:")
    if user=="Ready":
       Question=[
            "Who is the founder of Pakistan?" ,
            "1"
            ]
       print(Question[0])
user=input("To access options type(see):")
if user=="see":
          options=["1=Quaid-e-Azam" ,
                "2=Allama Iqbal" ,
                "3=Liaquat Ali Khan" , 
                "4=Sir Syed Ahmad Khan"]
          for option in options:
               print(option)
          user=input("CHOOSE CORRECT OPTION INTEGER:")
          if user==Question[1]:
               print("CONGRATULATION!You won $1000")
               user=input("IS YOU READY FOR NEXT QUESTIONS SO WE DISPLAY THEM: (Yes/No):")  
               if user=="Yes":
                    print("YOUR SECOND QUESTION AMOUNT IS $2000")
                    Question=[
                             "Which is the first Capital of Pakistan?" ,
                             "2"
                            ]
                    print(Question[0])
                    user=input("To access option type(see):")
                    if user=="see":
                         options=["1=Lahore" ,
                                  "2=Karachi" ,
                                  "3=Islamabad" , 
                             "4=Peshawar"]
                    for option in options:
                         print(option)
                    user=input("CHOOSE CORRECT OPTION INTEGER:")
                    if user==Question[1]:
                         print("CONGRATULATION!You won $2000")
                         print("Now!You won total $3000")
                         print("Your next Question Total amount is $3000")
                         print("Now!Your Third Question is:")
                         Question=[
                                   "Who wrote nation Anthem of Pakistan?" ,
                                   "2"
                                  ]
                         print(Question[0])
                         user=input("To see option type(see):")
                         if user=="see":
                             options=["1=Ahmed Faraz" ,
                                      "2=Hafeez Jalandhari" ,
                                      "3=Faiz Ahmed Faiz" ,
                                      "4=Allama Iqbal"]
                             for option in options:
                                  print(option)
                             user=input("CHOOSE CORRECT OPTION INTEGER:")
                             if user==Question[1]:
                                   print("CONGRATULATION!You won $3000")
                                   print("Total amount you won %6000")
                                   print("It's your last Question now.It's cover $4000")
                                   Question=[
                                             "When did Pakistan become independent?" ,
                                             "3"
                                            ]
                                   print(Question[0])
                                   user=input("To see option type(see):")
                                   options=["1=1949" ,
                                            "2=1946" ,
                                            "3=1947"  ,
                                            "4=1948"]
                                   for option in options:
                                        print(option)
                                   user=input("CHOOSE CORRECT OPTION INTEGER:")
                                   if user==Question[1]:
                                       print("CONGRATULATION!You won this game(KBC)")
                                       print("You won Total $10000")
                                   else:
                                       print("Wrong option!You loss $4000")
                                       print("YOU WON ONLY $6000 FROM $10000")
                             else:
                                  print("Wrong option!You loss $3000")
                                  print("YOU WON ONLY $3000 FROM $10000")
                    else:
                         print("Wrong option!You loss $2000")
                         print("YOU WON ONLY $1000 FROM $10000")
               else:
                    print("Okay!We give You $1000 that you won")
          else:
               print("Wrong option!You loss $1000")
     
          

      


       



