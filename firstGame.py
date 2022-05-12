print("\n Welcome to my first game")
name = input("Whats your name?: ") #input("what you type here takes input into variable")
age = int(input("whats your age?: "))
print("\n")
print("Hello " + name + "!")



lifePoints = 10

if age >= 18:
    print ("It looks like you're old enough to play this game!\n")

    askToPlay = input ("Do you want to play? (yes/no): ").lower()
    if askToPlay == "yes":
        print("Cool lets play!")
        print("Just so you know, you will begin with 10 health\n")

        print("You start your adventure and you come across a fork in the road")
        leftRight = input("Would you like to take the left or right path? (left/right): ").lower()

        if leftRight == "left":
            print("\nYou continue on the path until you come across a lake")
            print("You find a beat up boat that clearly has damage but you can't see how much damage it has")
            boatAns = input("Do you want to use the boat to cross? (yes/no):").lower()

            if boatAns == "yes":
                print("unfortunately the boat sprung a huge hole midway and you got dragged into the depths by a monster and died\n")

            else:
                print("Good choice! who knows how that boat wouldve been if we tried to use it\n")
                print("As you continue on with your journey, you find a rusty sword on the ground and equip it")
                print("Growl~, you realize that your stomach is growling so its time to hunt for some food")

                rabbit = input("You spot a rabbit, do you wish to fight it? (yes/no):").lower()
                if rabbit == "yes":
                    print("\n ouch the rabbit bit you, but you managed to defeat it")
                    print("-1 health")
                    lifePoints -= 1

                    print("current health: " , lifePoints)

        else:
            print("oh... goblins were waiting and they killed you....\n")


    else:
        print("Okay Good bye!\n")


else:

    print ("Sorry but youre too young to play.. good bye!\n")
