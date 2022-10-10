"""This is the data logic of the game as well as the interactive page of the game"""


#import statements
import random
from time import sleep
import sys
from tkinter import N
import TeamBlue
import TeamRed

# the kill switch to kick the user out the game whenever they use up all their lives


def gameover():
    if lives <= 0:
        # prints out all the attributes of each roles
        print(name, """
 ___  ___  ______    ____  ____           __        _______    _______         ______    ____  ____  ___________         ______    _______      ___        __  ___      ___  _______   ________           
|"  \/"  |/    " \  ("  _||_ " |         /""\      /"      \  /"     "|       /    " \  ("  _||_ " |("     _   ")       /    " \  /"     "|    |"  |      |" \|"  \    /"  |/"     "| /"       )          
 \   \  /// ____  \ |   (  ) : |        /    \    |:        |(: ______)      // ____  \ |   (  ) : | )__/  \\__/       // ____  \(: ______)    ||  |      ||  |\   \  //  /(: ______)(:   \___/           
  \\  \//  /    ) :)(:  |  | . )       /' /\  \   |_____/   ) \/    |       /  /    ) :)(:  |  | . )    \\_ /         /  /    ) :)\/    |      |:  |      |:  | \\  \/. ./  \/    |   \___  \             
  /   /(: (____/ //  \\ \__/ //       //  __'  \   //      /  // ___)_     (: (____/ //  \\ \__/ //     |.  |        (: (____/ // // ___)       \  |___   |.  |  \.    //   // ___)_   __/  \\  _____     
 /   /  \        /   /\\ __ //\      /   /  \\  \ |:  __   \ (:      "|     \        /   /\\ __ //\     \:  |         \        / (:  (         ( \_|:  \  /\  |\  \\   /   (:      "| /" \   :)))_  ")    
|___/    \"_____/   (__________)    (___/    \___)|__|  \___) \_______)      \"_____/   (__________)     \__|          \"_____/   \__/          \_______)(__\_|_)  \__/     \_______)(_______/(_____(     
                                                                                                                                                                                                          
  _______       __       ___      ___   _______         ______  ___      ___  _______   _______                                                                                                           
 /" _   "|     /""\     |"  \    /"  | /"     "|       /    " \|"  \    /"  |/"     "| /"      \                                                                                                          
(: ( \___)    /    \     \   \  //   |(: ______)      // ____  \\   \  //  /(: ______)|:        |                                                                                                         
 \/ \        /' /\  \    /\\  \/.    | \/    |       /  /    ) :)\\  \/. ./  \/    |  |_____/   )                                                                                                         
 //  \ ___  //  __'  \  |: \.        | // ___)_     (: (____/ //  \.    //   // ___)_  //      /                                                                                                          
(:   _(  _|/   /  \\  \ |.  \    /:  |(:      "|     \        /    \\   /   (:      "||:  __   \                                                                                                          
 \_______)(___/    \___)|___|\__/|___| \_______)      \"_____/      \__/     \_______)|__|  \___)                                                                                                         
                                                                                                                                                                                                          
""")
        print("your speed points are: ", speed)
        print("your agility points are: ", agility)
        print("your strength points are: ", strength)
        print("Your total points are", lives + speed + agility + strength)
        sys.exit()


print("""________                            ___      ___                
`MMMMMMMb.                           MM      `MM                
 MM    `Mb                           MM       MM                
 MM     MM ___   ___ ___  __    __   MM____   MM   ____         
 MM     MM `MM    MM `MM 6MMb  6MMb  MMMMMMb  MM  6MMMMb        
 MM    .M9  MM    MM  MM69 `MM69 `Mb MM'  `Mb MM 6M'  `Mb       
 MMMMMMM9'  MM    MM  MM'   MM'   MM MM    MM MM MM    MM       
 MM  \M\    MM    MM  MM    MM    MM MM    MM MM MMMMMMMM       
 MM   \M\   MM    MM  MM    MM    MM MM    MM MM MM             
 MM    \M\  YM.   MM  MM    MM    MM MM.  ,M9 MM YM    d9       
_MM_    \M\_ YMMM9MM__MM_  _MM_  _MM_MYMMMM9 _MM_ YMMMM9        
                                                            """)


# input to allow the user to pick a role to play within the game
classF = input("what size fighter, are you small or big ")
if (classF.lower() == "small"):
    cc = TeamBlue.smallFighter()
elif (classF.lower() == "big"):
    cc = TeamRed.bigFighter()
lives = cc[0]
speed = cc[1]
agility = cc[2]
strength = cc[3]
print(f"lives = {lives} speed = {speed} agil = {agility} str = {strength}")

# input which will assign a name with a variable
name = input("type in the name of the fighter ")
# empty print statements to create space
print()
print()
# sleep statement pauses the output for an amount of seconds
sleep(2.5)
print("welcome", name, "You will be our new prospect to fight against others to claim the Boxing championship title")
# empty print statements to create space
print()
print()
# sleep statement pauses the output for an amount of seconds
sleep(2.5)
print("""You will face multiple fights where you will roll dice 
to determine your success in landing punches and gaining points for your skill sets,
if you land on a number equal or less than 6, you will land your action, 
if the numbers are greater than 6, you will miss your action""")
# empty print statements to create space
print()
print()
# sleep statement pauses the output for an amount of seconds
sleep(5.5)
# prints out all the attributes of each roles
print("Prepare for your FIRST FIGHT!")
print("Your currrent lives are: ", lives)
print("your speed points are: ", speed)
print("your agility points are: ", agility)
print("your strength points are: ", strength)
print("Your current health is", lives, "hearts")
# empty print statements to create space
print()
print()

print("#################### Fight 1 ####################")
# empty print statements to create space
print()
print()
sleep(2.5)
print("Let's start the first fight, your first opponent is Manny Pacquiao. He's going to be a tough opponent but if you're lucky, you could beat him, GOOD LUCK!")
# empty print statements to create space
print()
print()

fight1 = input(
    "press l for a left hook, or u to have the fighter swing for a uppercut")
if fight1 == "l":
    print("The player sets up their footwork to go for a Left hook swing, you will land the punch if you roll a number lower or equal to 6")
elif fight1 == "u":
    print("The player gets below the opponent to swing for a uppercut, you will land the punch if you roll a number lower or equal to 6")
else:
    print("You didn't land on a number lower than 6, this resulted in you getting punched in the face")
# sleep statement pauses the output for 3 seconds
sleep(5.5)

# represent the rolling of two dice
die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1
# add the two die together
total = die1 + die2
# Print the outcome
print("You rolled a {} and a {} ".format(die1, die2) +
      "for a total of {}.".format(total))
if total <= 6:
    print("you have successfully landed your action, You win")
    speed = speed + 150
    agility = agility + 150
    strength = strength + 150
    sleep(2.5)
    # empty print statements to create space
    print()
    print()
    # prints out all the attributes of each roles
    print("your speed points are: ", speed)
    print("your agility points are: ", agility)
    print("your strength points are: ", strength)
    print("Your currently have", lives, "hearts")
elif total == 8:
    print("You landed on a 8, the match will result in a draw, you do not lose any lives nor do you gain any points")
    speed = speed + 0
    agility = agility + 0
    strength = strength + 0
    sleep(2.5)
    # empty print statements to create space
    print()
    print()
    # prints out all the attributes of each roles
    print("your speed points are: ", speed)
    print("your agility points are: ", agility)
    print("your strength points are: ", strength)
    print("Your currently have", lives, "hearts")
else:
    print("your action has missed, You lose")
    lives = lives - 1
    speed = speed + 0
    agility = agility + 0
    strength = strength + 0
    sleep(2.5)
    # empty print statements to create space
    print()
    print()
    # prints out all the attributes of each roles
    print("your speed points are: ", speed)
    print("your agility points are: ", agility)
    print("your strength points are: ", strength)
    print("Your current have", lives, "hearts left")
    gameover()
# sleep statement to pause the output for some time
sleep(2.5)
# empty print statements to create space
print()
print()

print("#################### Fight 2 ####################")
# empty print statements to create space
print()
print()

# three quotation marks are used to break down the print statement text
print("""We will continue on to the next fight, your next opponent will be Floyd Mayweather jr. 
He's ranked 5th for being one of the best boxers in the world, if you win you will gain more points, GOOD LUCK!""")
# empty print statements to create space
print()
print()

fight2 = input(
    "press r for a right hook, or s to have the fighter swing for a punch in the stomach ")
if fight2 == "r":
    print("The player sets up their footwork to go for a right hook swing, you will land the punch if you roll a number lower or equal to 6")
elif fight2 == "s":
    print("The player faces sideways to get a swing for the stomach, you will land the punch if you roll a number lower or equal to 6")
else:
    print("You didnt land on a number lower than 6, this resuted in you getting punched in the face")
# sleep statement pauses the output for 3 seconds
sleep(5.5)

# represent the rolling of two dice
die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1
# add the two die together
total = die1 + die2
# Print the outcome
print("You rolled a {} and a {} ".format(die1, die2) +
      "for a total of {}.".format(total))
if total <= 6:
    print("you have successfully landed your action, You win")
    speed = speed + 250
    agility = agility + 250
    strength = strength + 250
    sleep(2.5)
    # empty print statements to create space
    print()
    print()
    # prints out all the attributes of each roles
    print("your speed points are: ", speed)
    print("your agility points are: ", agility)
    print("your strength points are: ", strength)
    print("Your currently have", lives, "hearts")
elif total == 8:
    print("You landed on a 8, the match will result in a draw, you do not lose any lives nor do you gain any points")
    speed = speed + 0
    agility = agility + 0
    strength = strength + 0
    sleep(2.5)
    # empty print statements to create space
    print()
    print()
    # prints out all the attributes of each roles
    print("your speed points are: ", speed)
    print("your agility points are: ", agility)
    print("your strength points are: ", strength)
    print("Your currently have", lives, "hearts")
else:
    print("your action has missed, You lose")
    lives = lives - 1
    speed = speed + 0
    agility = agility + 0
    strength = strength + 0
    sleep(2.5)
    # empty print statements to create space
    print()
    print()
    # prints out all the attributes of each roles
    print("your speed points are: ", speed)
    print("your agility points are: ", agility)
    print("your strength points are: ", strength)
    print("Your current have", lives, "hearts left")
    # empty print statements to create space
    print()
    print()
    gameover()
    # empty print statements to create space
    print()
    print()
# sleep statement to pause the ouput for some time
sleep(2.5)

print("#################### Fight 3 ####################")
# empty print statements to create space
print()
print()

print("""Congradulations, you have reached the final fight, you will verse the legedary boxer Muhammad Ali for the Championship title, 
He's going to be the hardest to fight. But if your lucky, you could win, GOOD LUCK!""")
# empty print statements to create space
print()
print()

fight3 = input(
    "press ru for a rear-uppercut, or lh to have the fighter swing for lead hook")
if fight3 == "ru":
    print("The player sets up their footwork to go for a rear-uppercut swing, you will land the punch if you roll a number lower or equal to 6")
elif fight3 == "lh":
    print("The player faces the opponent and swings for a lead hook, you will land the punch if you roll a number lower or equal to 6")
else:
    print("You didnt land on a number lower than 6, this resuted in you getting punched in the face")
# sleep statement pauses the output for 3 seconds
sleep(5.5)

# represent the rolling of two dice
die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1
# add the two die together
total = die1 + die2
# Print the outcome
print("You rolled a {} and a {} ".format(die1, die2) +
      "for a total of {}.".format(total))
if total <= 6:
    print("you have successfully landed your action, You win")
    speed = speed + 600
    agility = agility + 600
    strength = strength + 600
    sleep(2.5)
    # empty print statements to create space
    print()
    print()
    # prints out all the attributes of each roles
    print("your speed points are: ", speed)
    print("your agility points are: ", agility)
    print("your strength points are: ", strength)
    print("Your currently have", lives, "hearts")
elif total == 8:
    print("You landed on a 8, the match will result in a draw, you do not lose any lives nor do you gain any points")
    speed = speed + 0
    agility = agility + 0
    strength = strength + 0
    sleep(2.5)
    # empty print statements to create space
    print()
    print()
    # prints out all the attributes of each roles
    print("your speed points are: ", speed)
    print("your agility points are: ", agility)
    print("your strength points are: ", strength)
    print("Your currently have", lives, "hearts")
else:
    print("your action has missed, You lose")
    lives = lives - 1
    speed = speed + 0
    agility = agility + 0
    strength = strength + 0
    sleep(2.5)
    # empty print statements to create space
    print()
    print()
    # prints out all the attributes of each roles
    print("your speed points are: ", speed)
    print("your agility points are: ", agility)
    print("your strength points are: ", strength)
    print("Your current have", lives, "hearts left")
    # empty print statements to create space
    print()
    print()
    gameover()
# sleep statement to pause the ouput for some time
sleep(2.5)
# empty print statements to create space
print()
print()
# prints out all the attributes of each roles at the end of the
print("WELL DONE, you WON THE CHAMPIONSHIP TITLE")
print("You have", lives, "hearts left")
print("your speed points are: ", speed)
print("your agility points are: ", agility)
print("your strength points are: ", strength)
print("Your total points are", lives + speed + agility + strength)
print("GAME OVER")
