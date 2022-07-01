#Time function brought in for delay to make program feel more real. 
import time

#I wanted to start with a welcome and make sure the user knew what to expect with the game. 
print ("""Thank you for playing Mad Libs!!! 
Please enter the following 6 words: """)

#Added color to the words the player inputted to make them stand out a bit. 
Adjective = input("An adjective: \033[31m")
Adjective_Lower = Adjective.lower() #Ensuring correct case. 
Animal = input("\033[39mAn animal: \033[32m")
Animal_Lower = Animal.lower () #Ensuring correct case. 
Adverb = input("\033[39mAn adverb (ends with ing): \033[33m")
Adverb_Lower = Adverb.lower() #Ensuring correct case. 
Exclamation = input("\033[39mAn exclamation (something you might shout in the heat of the moment): \033[34m")
Exclamation_Upper = Exclamation.upper() #Ensuring correct case. 
Verb_1 = input("\033[39mA verb (no ing): \033[35m")
Verb_1_Lower =Verb_1.lower() #Ensuring correct case. 
Verb_2 = input("\033[39mAnd lastly a 2nd verb (no ing): \033[36m")
Verb_2_Lower = Verb_2.lower() #Ensuring correct case. 


print("") #Added aesthetic appeal. 
print("\033[39mGenerating Mad Lib ...") #Added to make the program feel more real. 
time.sleep (3) #Added to make the program feel more real. 
print("") #Added aesthetic appeal. 

#Deliberately broke up dialog by sentance to ensure better readability. 
Output = (f"""The other day, I was really in trouble. 
It all started when I saw a very \033[31m{Adjective_Lower} \033[32m{Animal_Lower} \033[33m{Adverb_Lower}\033[39m down the hallway.
\033[34m{Exclamation_Upper}\033[39m! I yelled. 
But all I could think to do was to \033[35m{Verb_1_Lower}\033[39m over and over. 
Miraculously, that caused it to stop, but not before it tried to \033[36m{Verb_2_Lower} \033[39mright in front of my family.""")
print(Output)

#Future goals: Try to figure out how to give the user the choice to auto restart the program via answering a question. 