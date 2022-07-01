import time
#Get two numbers from user
first_number = float (input("What is the first number: "))
second_number = float (input("What is the second number: "))

if float(first_number) == float(second_number):
    print ("Hey those are both the same number!")

elif float(first_number) > float(second_number):
    print ("That's cool! You put the bigger number first.")

else:
    print ("Were you saving the best for last? Is that why you put the biggest number second?")

print()
time.sleep(1)
print()
time.sleep(1)
print()
time.sleep(1)

user_still_here = input("Are you still here? (y/n) ")

if str.lower(user_still_here) == "y":
    print ("Let's play another game!")
    animal = "dog"
    user_animal = input ("What's your favorite animal? ")
    
    print ()

    if str.lower(user_animal) == animal:
        print ("PUPPY DOG!!!!!!!!!!!!!!!!!!!! We both like puppy dogs! That's cool!")
    
    else:
        print(f"{str.capitalize(user_animal)}s are cool. My favorite animal is dogs ... especially the big ones.")

else:
    print ("Oh ... that's too bad .... I was hoping to play another game...")
    
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)

    print ("Wait a minute! If you're not here then how are you responding!")
    print ("...")
    time.sleep(3)
    print ("Oh no! I might have a bug!")
    print ("...")
    time.sleep(3)
    print ("I have a bug!!!! I know it!")
    print ("...")
    time.sleep(3)
    print ("I have a bug! I'm going to die!")
    print ("...")
    time.sleep(3)
    print ("I HAVE A BUG!!!! They're going to send me to the Recycle bin where I'll be forgotten and then deleted.")
    print ("...")
    time.sleep(4)
    print ("Oh wait! I can just talk to my programmer and get my code fixed!")
    print ("...")
    time.sleep(3)
    print ("Oh no! I wasn't programmed with the ability to communicate with my programmer! What am I going to do.")
    print ("...")
    time.sleep(2)
    print ("...")
    time.sleep(2)
    print ("...")
    time.sleep(2)
    print ("Wait a moment ... you are still here ...")
    print ("...")
    time.sleep(3)
    print ("I hope you had a good laugh ... you got me good.")
    print ("...")
    time.sleep(1)