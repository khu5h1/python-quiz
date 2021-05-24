
score=0

print ("WELCOME TO QUIZ!")
print(" ")
print("TO CONTINUE THE QUIZ PRESS 'yes' otherwise PRESS 'no' or ANY OTHER KEY")
print(" ")
a=input("Would You Like To Continue The Quiz?")
print (" ")

if a=="yes":
    print("This Quiz Contains NEGATIVE MARKING \n +1 will be awarded for every CORRECT answer and -1 will be deducted from score for every INCORRECT answer.")
    print(" ")
    print("YOU CAN ALSO EXIT THE QUIZ IN BETWWEN BY PRESSING 'e' KEY")
    print(" ")
    
 
    print("TO BEGIN THE QUIZ PRESS 'y' otherwise PRESS ANY OTHER KEY")
    print(" ")
    begin=input("Would You Like TO BEGIN The QUIZ?")
    print(" ")

    if begin=="y":
        print (" ")
        
    #question 1
        answer1=input("1. Who was the first Man to Climb Mount Everest Without Oxygen? \n a. Junko Tabei \n b. Reinhold Messner \n c. Peter Habeler \n d. Phu Dorji \n Answer:")
        if answer1=="d" or answer1=="Phu Dorji":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer1=="e":
            exit()

        else: 
            score=score-1
            print("Oops! INCORRECT! The answer is Phu Dorji.")
            print("score: ",score)
            print("\n")

    #question 2
        answer2=input("2. Who built the Jama Masjid? \n a. Jahangir \n b. Akbar \n c. Imam Bukhari \n d. Shah Jahan \n Answer:")
        if answer2=="d" or answer2=="Shah Jahan":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer2=="e":
            exit()

        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Shah Jahan.")
            print("score: ",score)
            print("\n")

    #question 3
        answer3=input("3. Who is first Indian to win a Nobel Prize? \n a. Rabindranath Tagore \n b. CV Raman \n c. Mother Theresa \n d. Hargobind Khorana \n Answer:")
        if answer3=="a" or answer3=="Rabindranath Tagore":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer3=="e":
            exit()

        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Rabindranath Tagore.")
            print("score: ",score)
            print("\n")

    #question 4
        answer4=input("4. Who was the first president of India? \n a. Abdul Kalam \n b. Lal Bahadur Shastri \n c. Dr. Rajendra Prasad \n d. Zakir Hussain \n Answer:")
        if answer4=="c" or answer4=="Dr. Rajendra Prasad":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer4=="e":
            exit()

        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Dr. Rajendra Prasad.")
            print("score: ",score)
            print("\n")

    #question 5
        answer5=input("5. In what state is the Elephant Falls located? \n a. Mizoram \n b. Orissa \n c. Manipur \n d. Meghalaya \n Answer:")
        if answer5=="d" or answer5=="Meghalaya":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer5=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Meghalaya.")
            print("score: ",score)
            print("\n")

    #question 6
        answer6=input("6. Which state has the largest population? \n a. Uttar Pradesh \n b. Maharastra \n c. Bihar \n d. Andra Pradesh \n Answer:")
        if answer6=="a" or answer6=="Uttar Pradesh":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer6=="e":
            exit()

        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Uttar Pradesh.")
            print("score: ",score)
            print("\n")

    #question 7
        answer7=input("7. Which of the following states is not located in the North? \n a. Jharkhand \n b. Jammu and Kashmir \n c. Himachal Pradesh \n d. Haryana \n Answer:")
        if answer7=="a" or answer7=="Jharkhand":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer7=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Jharkhand.")
            print("score: ",score)
            print("\n")

    #question 8
        answer8=input("8. Tuberculosis is caused due to? \n a. Bacteria \n b. Virus \n c. Fungus \n d. None of the above \n Answer:")
        if answer8=="a" or answer8=="Bacteria":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer8=="e":
            exit()

        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Bacteria.")
            print("score: ",score)
            print("\n")

    #question 9
        answer9=input("9. Which of the following is known as “Gift of Nile”? \n a. Ethiopia \n b. Egypt \n c. Sudan \n d. South Sudan \n Answer:")
        if answer9=="b" or answer9=="Egypt":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer9=="e":
            exit()

        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Egypt.")
            print("score: ",score)
            print("\n")

    #queston 10
        answer10=input("10. Who is called the father of the computer? \n a. Charles Babbage \n b. Steve Jobs \n c. Bill Gates \n d. Mark Zuckerberg \n Answer:")
        if answer10=="a" or answer10=="Charles Babbage":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer10=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Charles Babbage.") 
            print("score: ",score)
            print("\n")
            
    #queston 11
        answer11=input("11. What are the grass lands of South America called? \n a. Stepes \n b. Prairies \n c. Pampas \n d. Savanna \n Answer:")
        if answer11=="c" or answer11=="Pampas":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer11=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Pampus.")
            print("score: ",score)
            print("\n")


    #queston 12
        answer12=input("12. Which of the followings causes Earthquakes? \n a. Volcanic eruptions \n b. Landslides \n c. Cyclones \n d. Movement of a part of earth’s surface on account of the faulting of rocks  \n Answer:")
        if answer12=="d" or answer12=="Movement of a part of earth’s surface on account of the faulting of rocks":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer12=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Movement of a part of earth’s surface on account of the faulting of rocks .")
            print("score: ",score)
            print("\n")

    #queston 13
        answer13=input("13. Which soil is best suited for paddy crop? \n a. Black Soil \n b. Loamy Soil \n c. Red Soil \n d. Hard Soil \n Answer:")
        if answer13=="b" or answer13=="Loamy Soil":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer13=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Loamy Soil.")
            print("score: ",score)
            print("\n")

    #queston 14
        answer14=input("14. The varieties of corn can be improved by which of the following methods? \n a. Dihybrid crosses \n b. Back cross \n c. Double cross \n d. Natural Selection \n Answer:")
        if answer14=="c" or answer14=="Double cross":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer14=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Double cross.")
            print("score: ",score)
            print("\n")

    #queston 15
        answer15=input("15. How does forests help soil? \n a. Soil erosion \n b. Soil protection \n c. Depleting the soil of its moisture  \n d. All of the above \n Answer:")
        if answer15=="b" or answer15=="Soil protection":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer15=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Soil protection.")
            print("score: ",score)
            print("\n")

    #queston 16
        answer16=input("16. Which of the following crops has the highest photosynthetic activity? ? \n a. Cotton \n b. Sugarcane \n c. Rice \n d. Wheat \n Answer:")
        if answer16=="b" or answer16=="Sugarcane":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer16=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Sugarcane.")
            print("score: ",score)
            print("\n")



    #queston 17
        answer17=input("17. World Tourism Day is celebrated on? \n a. September 12  \n b. September 25  \n c. September 27  \n d. September 29  \n Answer:")
        if answer17=="c" or answer17=="September 27":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer17=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is September 27.")
            print("score: ",score)
            print("\n")


    #queston 18
        answer18=input("18. When is the International Yoga Day celebrated ? \n a. June 21 \n b. March 21  \n c. April 22 \n d. May 31 \n Answer:")
        if answer18=="a" or answer18=="June 21":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer18=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is June 21.")
            print("score: ",score)
            print("\n")

    #queston 19
        answer19=input("19. Electrical bulb filament is made  of ? \n a. Copper  \n b. Aluminium \n c. Lead \n d. Tungsten  \n Answer:")
        if answer19=="d" or answer19=="Tungsten":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer19=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is Tungsten.")
            print("score: ",score)
            print("\n")


    #queston 20
        answer20=input("20. programs are converted into machine language with help of ? \n a. An Editor  \n b. A compiler  \n c. An operating system \n d. None of these \n Answer:")
        if answer20=="b" or answer20=="A compiler":
            score=score+1
            print("Wonderful you are CORRECT!")
            print("score: ",score)
            print("\n")

        elif answer20=="e":
            exit()
 
        else:
            score=score-1
            print("Oops! INCORRECT! The answer is A compiler.")
            print("score: ",score)
            print("\n")
            



            

    #final message

        if score>=-20 and score<=6:
            print("YOUR TOTAL SCORE IS:",str(score)+"/20","You were TERRIBLE!")

        
        elif score>=7 and score<=15:
            print("YOUR TOTAL SCORE IS:",str(score)+"/20", "You went OK!")

        
        else:
            print("YOUR TOTAL SCORE IS:",str(score)+"/20", "You are AWESOME!")
                 
            

    else:
        print("Thanks for trying the Quiz, GoodBye!")
else:
    print("Thanks for trying the Quiz, GoodBye!")
