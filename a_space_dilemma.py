#***************************************************************************
# a_space_dilemma.py
# A SPACE DILEMMA - a game developed by the group 3 development team
# Created by the GROUP 3 Development team - Badra, Mikael and Colin
#***************************************************************************
# 
#   import required libraries / functions
#
#***************************************************************************
import sys          # import system functions library
import random       # import random functions library
import winsound     # import the sounds library functions
#***************************************************************************
#
# define all modules / subroutines to be used
#
#***************************************************************************
def make_sound(sound_file):
    winsound.PlaySound(sound_file,winsound.SND_FILENAME)
#***************************************************************************
def get_game_details():
#   get users name and # sound is required or not ...
    global user_name 
    user_name = str(input("Please enter your name: "))
#    sound_ask = upper(input("Would you like sound on? (Y/N): "))
#    if sound_ask == "Y" or sound_ask == "y":
#        sound_on = True
#***************************************************************************
def check_int():
    valid_input = False
    user_input = 99 
    global early_exit

    while valid_input != True:
        #   enable error trapping ... 
        try:
            # prompt user for choice
            user_input = int(input("Enter Option Choice, 1-4 : "))

#            if user_input == 0:
#                valid_input = True  # if we get this far then user has entered an integer in range 0-4
#                early_exit_selected(user_name) # option selected is 0 - early exit
#                closing_credits(user_name)
#                early_exit = True
#                sys.exit()  # raise error to terminate program

            if user_input >= 1 and user_input <=4:
                valid_input = True  # if we get this far then user has entered an integer in range 0-4
                return user_input     # return valid user selection in range 1 - 4, or 0 to exit
            else:   # numbers - but not in range 0 to 4
                print("\nInvalid option selected ... please try again (1-4)".format(user_input))

        except TypeError:  # trap data type errors
            print("\nInvalid option selected ... please try again (1-4)".format(user_input))

        except ValueError: # trap value errors
            print("\nInvalid option selected ... please try again (1-4)".format(user_input))

        except:            # trap any other non-integer errors
            print("\nInvalid option selected ... please try again (1-4)".format(user_input))

#        finally:
#            continue()
#***************************************************************************
def input_options(opt1, opt2, opt3, opt4):
    print("Option 1: {}\nOption 2: {}\nOption 3: {}\nOption 4: {} : ".format(opt1, opt2, opt3, opt4))
#***************************************************************************
def early_exit_selected(user_name):
    print("\n\nEarly exit option chosen ... goodbye {} and thanks for playing\n\n".format(user_name))
    make_sound("abort.wav")
#   display closing text / thank you 
    closing_credits()
    sys.exit()  # raise error to terminate program
#***************************************************************************
def random_generate(start_pos, end_pos):
    return int(random.randint(start_pos,end_pos)) # generate a random number between start_pos and end_pos
#***************************************************************************
def random_generate_boolean(start_pos, end_pos):
    if int(random.randint(start_pos,end_pos)) == 1:  # generate a random number between start_pos and end_pos
        return True
    else:
        return False
#***************************************************************************
def check_comms():
    global comm_desc
    global comm_health
    if comm_health < 0:
        comm_health = 0    
    elif comm_health > 100:
        comm_health = 100    
    print("COMM STATUS: {}, Health: {} %\n".format(comm_desc, comm_health))
#*********************************************************************
def check_oxygen():
    global oxygen_desc
    global oxygen_health
    if oxygen_health < 0:
        oxygen_health = 0    
    elif oxygen_health > 100:
        oxygen_health = 100    
    print("OXYGEN STATUS: {}, Health: {} %\n".format(oxygen_desc,oxygen_health))
#*********************************************************************
def check_team():
    print("TEAM STATUS: \n{} : {}, Health: {} %".format(crew1_name, crew1_skill, crew1_health))  
    print("{} : {}, Health: {} %".format(crew2_name, crew2_skill, crew2_health))  
    print("{} : {}, Health: {} %".format(crew3_name, crew3_skill, crew3_health))  
    print("{} : {}, Health: {} %".format(crew4_name, crew4_skill, crew4_health))  
    print("{} : {}, Health: {} %\n".format(user_name, "Player", user_health))  
#*********************************************************************
def check_all():
#   show all statuses
    check_team()
    check_oxygen()
    check_comms()
#*********************************************************************
def check_health_GT_100():
#   check that the health cannot be greater than 100
    global crew1_health
    global crew2_health
    global crew3_health
    global crew4_health
    global crew5_health
    global user_health
    global oxygen_health
    global comm_health

    if crew1_health > 100:
        crew1_health = 100
    if crew2_health > 100:
        crew2_health = 100
    if crew3_health > 100:
        crew4_health = 100
    if crew4_health > 100:
        crew4_health = 100
    if user_health > 100:
        user_health = 100
    if oxygen_health > 100:
        oxygen_health = 100
    if comm_health > 100:
        comm_health = 100
#*********************************************************************
def check_health_LT_0():
#   check if user or crew health less than 0
    global crew1_health
    global crew2_health
    global crew3_health
    global crew4_health
    global crew5_health
    global user_health
    global oxygen_health
    global comm_health

    if crew1_health <= 0:
        crew1_health = 0
    if crew2_health <= 0:
        crew2_health = 0
    if crew3_health <= 0:
        crew3_health = 0
    if crew4_health <= 0:
        crew4_health = 0
    if user_health <= 0:
        user_health = 0
    if oxygen_health < 0:
        oxygen_health = 0
    if comm_health <= 0:
        comm_health = 0
#***************************************************************************
def check_toolbox():
#    print("Spanner: {}, Hose: {}, Welder: {}, Comms Card: {}".format(toolbox_spanner, toolbox_hose, toolbox_welder, toolbox_comms_card))
    print("TOOLBOX STATUS: Spanner: TRUE, Hose: TRUE, Welder: TRUE, Comms Card: TRUE")
#***************************************************************************
def general_error(which_scenario):
    global crew1_health
    global crew2_health
    global crew3_health
    global crew4_health
    global crew5_health
    global user_health
    global oxygen_desc
    global oxygen_health
    global comm_desc
    global comm_health

#     make_sound("doh.wav")
    crew1_health -= 5
    crew2_health -= 5
    crew3_health -= 5
    crew4_health -= 5
    user_health -= 5

    check_health_LT_0()  # test / rectify if any crew / user health < 0

    print("\nZED: OOOPS.... BAD OPTION CHOICE {}, THERE'S A 5 POINT HEALTH REDUCTION ALL AROUND\n".format(user_name))

    if which_scenario == "scenario_1" :
#       SCENARIO 1 - OXYGEN - INTERNAL
        oxygen_health -= 5        
    elif which_scenario == "scenario_2" :
#       SCENARIO 2 - OXYGEN - EXTERNAL
        oxygen_health -= 5        
    elif which_scenario == "scenario_3" :
#       SCENARIO 3 - COMMS - INTERNAL
        comm_health -= 5        
    elif which_scenario == "scenario_4" :
#       SCENARIO 4 - COMMS - EXTERNAL
        comm_health -= 5        
    else:
        print("INVALID call to general_error routine")
        make_sound("doh.wav")

    check_all()
#***************************************************************************
def run_reward(which_scenario):
    global crew1_health
    global crew2_health
    global crew3_health
    global crew4_health
    global crew5_health
    global oxygen_desc
    global oxygen_health
    global comm_desc
    global comm_health
    global user_health

    make_sound("APPLAUSE.WAV")
    crew1_health += 15
    crew2_health += 15
    crew3_health += 15
    crew4_health += 15
    user_health += 15

    check_health_GT_100()  # test / rectify if any crew / user health > 100

    if which_scenario == "scenario_1" :
        print("\nZED: HEY, {}, YOU HAVE SOLVED THE OXYGEN INTERNAL PROBLEM! YOU GENIUS!".format(user_name)) 
        print("\nBONUS points and health improvements all round!!!!... :o)\n")
        oxygen_health += 25        
        oxygen_desc = "Oxygen INTERNAL issue fixed, EXTERNAL issue still needs repair"
        check_oxygen()
    elif which_scenario == "scenario_2" :
        print("\nZED: WELL DONE {}, YOU HAVE NOW SOLVED THE OXYGEN EXTERNAL PROBLEM!".format(user_name)) 
        print("\nBONUS points and health improvements all round!... :o)")
        oxygen_desc = "Oxygen INTERNAL and EXTERNAL issues all fixed"
        oxygen_health += 25        
        check_oxygen()
    elif which_scenario == "scenario_3" :
        print("\nZED: HELLO, {}, CAN YOU HEAR ME?... KIDDING! YOU HAVE SOLVED THE COMMS INTERNAL PROBLEM! YOU ARE ON A ROLL!".format(user_name)) 
        print("\nBONUS points and health improvements all round!  ... :o)")
        comm_desc = "COMMS INTERNAL issue fixed, EXTERNAL issue still needs repair"
        comm_health += 25        
        check_comms()
    elif which_scenario == "scenario_4" :
        print("\nZED: {}, THE COMMS EXTERNAL PROBLEM HAS BEEN SOLVED, TAKE A BOW, GO ON... YOU KNOW YOU WANT TO...".format(user_name)) 
        print("\nBONUS points and health improvements all round!  ... :o)")
        comm_desc = "COMMS INTERNAL and EXTERNAL issues all fixed"
        comm_health += 25        
        check_comms()
    else:
        print("INVALID call to run_reward routine")
        make_sound("doh.wav")
#***************************************************************************
def opening_credits(user_name):
#   display opening credits / game scenario
    print("Opening scene .....\n")
    print("Welcome {}\n".format(user_name))
    print("YOU ARE RETURNING HOME FROM A MISSION, WHEN SUDDENLY YOU PICK UP A DISTRESS MESSAGE")
    print("OVER YOUR INTERCOM FROM A SPACESHIP NEARBY, EXPLAINING THAT THE CREW IS SERIOUSLY INJURED AND") 
    print("THE SHIP HAS TAKEN HEAVY DAMAGE.\n")
    print("YOU DECIDE TO GO INVESTIGATE...\n")
    print("UPON NEARING THE SPACESHIP, YOU NOTICE IT IS FREE FLOATING IN SPACE AND IS")
    print("SURROUNDED BY DEBRIS...\n")
    print("BEING IN A ONE MAN SHIP YOURSELF, IT’S EASY TO NAVIGATE AROUND AND DOCK YOUR SHIP")
    print("AS CLOSE AS POSSIBLE.\n")
    print("YOU BOARD THE DAMAGED SPACESHIP... WITH NO IDEA WHAT TO EXPECT...\n")
    
    if sound_on == True:
        make_sound("20th_century_fox.wav")
#  
#***************************************************************************
def closing_credits():
#   display closing credits / thank you
    print("\nZED: NOW, I KNOW WHAT YOU'RE THINKING... WHAT ABOUT THE CREW MEMBERS?")
    print("THERE'S SO MUCH I DON'T UNDERSTAND!")
    print("WELL, FOR $9.99 YOU CAN GET THE DLC THAT EXPLAINS IT ALL.")
    print("\n\nThank you for playing {} ... \n\n".format(user_name))
    print("This game has been brought to you by the GROUP 3 Development team\n")
    print("               BADRA\n")
    print("               MIKAEL\n")
    print("               COLIN\n")
    print("\n\nWe are available for other projects, weddings, picnics, pub crawls ....\n\n")
    print("\n\n\nHave a nice day! ... \n\n")

    #   if sound_on == True:
    make_sound("APPLAUSE.WAV")
#***************************************************************************
def anykey_to_continue():
#   pause for the user to hit anykey
    make_sound("anykey.wav")
    dummy_pause = input("Press any key to continue ... ")
#***************************************************************************
def test_input():
    input_options("Check team status","Check Comms status","Check Oxygen status","Check toolbox")
    my_input = check_int() # test / verify user input

    #   while my_input != 0:
    if my_input == 0:
        early_exit_selected(user_name) # option selected is 0 - early exit
        closing_credits(user_name)
        sys.exit()  # raise error to terminate program
    elif my_input == 1:
        check_team()
    elif my_input == 2:
        check_comms()
    elif my_input == 3:
        check_oxygen()
    elif my_input == 4:
        check_toolbox()
    else:
        print("Invalid Option")
#
#    print("\n")
#    my_input = check_int() # ask for users next input option / verify user input
#***************************************************************************
def set_initial_statuses():
    # declare variable / globals / randomized values
    # Set initial and randomised parameters ... 
    # Variable declared as global can be used in other modules
    global ship_oxygen_level
    ship_oxygen_level = 100     # crew ship oxygen % level (1 hour)

    global crew1_name
    global crew2_name
    global crew3_name
    global crew4_name
    global crew5_name
    global crew1_skill
    global crew2_skill
    global crew3_skill
    global crew4_skill
    global crew5_skill
    global crew1_health
    global crew2_health
    global crew3_health
    global crew4_health
    global crew5_health
    crew1_name = "Jack"  	    # set crew & android names  
    crew2_name = "Paul"  	    # set crew & android names  
    crew3_name = "Jane"  	    # set crew & android names  
    crew4_name = "Sue"  	    # set crew & android names  
    crew5_name = "ZED"          # set crew & android names
    crew1_skill = "Pilot"       # set crew roles / skills
    crew2_skill = "Comms"       # set crew roles / skills
    crew3_skill = "Doctor"      # set crew roles / skills
    crew4_skill = "Mechanic"    # set crew roles / skills
    crew5_skill = "Android"     # set crew roles / skills
    crew1_health = random_generate(50, 100) # randomise crew member health between 50 and 100 %
    crew2_health = random_generate(50, 100) # randomise crew member health between 50 and 100 %
    crew3_health = random_generate(50, 100) # randomise crew member health between 50 and 100 %
    crew4_health = random_generate(50, 100) # randomise crew member health between 50 and 100 %
    crew5_health = random_generate(50, 100) # randomise crew member health between 50 and 100 %
    #
    global user_health
    user_health = 100         # players health defaults to 100% at start of game
    #
    global player_passenger_seats
    player_passenger_seats = 1  # random_generate(1, 3) # randomise players passenger seats between 1 and 2
    #
    global comm_desc    # = "default desc"
    global comm_health  # = "default health"
    global comm_fix     # = "default fix"
    comm_status = random_generate(1, 4)     # randomise comms status 1 - 4
#
#   for the purposes of our demo ... comm_status will be set to 4
#
    comm_status = 4
    if comm_status == 1:
        comm_desc = "Full comms available"
        comm_health = 100
        comm_fix = "No fix required"    
        scenario_3_complete = True
        scenario_4_complete = True
    elif comm_status == 2:
        comm_desc = "Damaged comms INTERIOR fix required"   #   (fix requires comms card)  
        comm_health = 50
        comm_fix = "Comms card required"
        scenario_3_complete = False
        scenario_4_complete = True
    elif comm_status == 3:
        comm_desc = "Damaged comms EXTERIOR Space walk fix required"
        comm_health = 50
        comm_fix = "Space Walk and spanner required"
        scenario_3_complete = True
        scenario_4_complete = False
    else:   
        comm_desc = "Extensive Damage to comms INTERIOR and EXTERIOR fixes required"     
        comm_health = 0
        comm_fix = "Comms Card AND Space walk with spanners fixes required" #  fix requires comms card & spanners
        scenario_3_complete = False
        scenario_4_complete = False         
#    COMMENTED OUT - FUTURE USE 
#    print("COMM STATUS: {}, Health: {}%".format(comm_desc, comm_health))
#
#    toolbox_location = random_generate(1, 2)  # randomise toolbox location status 1 - 2
#    if toolbox_location == 1:
#        toolbox_to_hand = True              # toolbox on crews ship
#    else:
#        toolbox_to_hand = False             # toolbox on players ship

#   toolbox_status = random_generate(1, 2)  # randomise contents of toolbox 1 - 3
#   if toolbox_status == 1:                 # Full toolbox
    global toolbox_spanner
    global toolbox_hose
    global toolbox_comms_card
    global toolbox_welder    
    toolbox_spanner = True
    toolbox_hose = True
    toolbox_welder = True
    toolbox_comms_Card = True
#   COMMENTED OUT - FUTURE USE
 #   elif toolbox_status == 2:             # Partial toolbox randomise tools
 #       toolbox_spanner = random_generate_boolean(1,2)
 #       toolbox_hose = random_generate_boolean(1,2)
 #       toolbox_welder = random_generate_boolean(1,2)
 #       toolbox_comms_Card = random_generate_boolean(1,2)
 #   elif toolbox_status == 3:             # Empty toolbox 
 #       toolbox_spanner = False
 #       toolbox_hose = False
 #       toolbox_welder = False
 #       toolbox_comms_Card = False
#
    global oxygen_desc
    global oxygen_health
    global oxygen_fix
    oxygen_status = random_generate(1, 4)     # randomise oxygen status 1 - 4
#
#   for the purposes of our demo ... oxygen_status will be set to 4
#
    oxygen_status = 4
    if oxygen_status == 1:
        oxygen_desc = "Full Oxygen available"
        oxygen_fix = "No fix required"    
        oxygen_health = 100
        scenario_1_complete = True
        scenario_2_complete = True         
    elif oxygen_status == 2:
        oxygen_desc = "Damaged oxygen INTERIOR fix required"   #   (fix requires oxygen hose)  
        oxygen_fix = "Oxygen hose and sealant fix required"
        oxygen_health = 75
        scenario_1_complete = False
        scenario_2_complete = True         
    elif oxygen_status == 3:
        oxygen_desc = "Damaged oxygen EXTERIOR Space walk fix required"
        oxygen_health = 75
        scenario_1_complete = True
        scenario_2_complete = False         
    else:   
        oxygen_desc = "Extensive Damage to oxygen INTERIOR and EXTERIOR fixes required"     
        oxygen_fix = "Oxygen hose AND Space walk fixes required" #  fix requires oxygen hose and space walk welding
        oxygen_health = 50
        scenario_1_complete = False
        scenario_2_complete = False         
#
    global mothership_time
#    mothership_distance = random_generate(1, 3)     # randomise mothership distance 1 - 3
#    if mothership_distance == 1:
#        mothership_time = 60        # 1 hour
#    elif mothership_distance == 2:
    mothership_time = 120       # 2 hours
#    else: mothership_time = 180     # 3 hours
#***************************************************************************

def scenario_1():
#***************************************************************************
#   SCENARIO 1 - OXYGEN Internal issue
#***************************************************************************
    # <<<<<<< User game dialogue text here ... >>>>
    print("\n\nThe ships android ZED greets you and tells you that they have extensive")
    print("damage, the crew members are trapped 3 levels above and there's currently no way") 
    print("to get to them. Also, the Oxygen generator and the Communications systems are affected\n")
    print("\nZED: I HAVE SYNCHRONISED OUR INTERCOM SO WE CAN COMMINICATE WITH EACH OTHER.")
    print("I WILL ALSO KEEP YOU UPDATED WITH THE CREW'S VITAL SIGNS AS YOU PROGRESS. ") 
    print("NOW FIRST, YOU WILL FIND THE OXYGEN CHAMBER ON THE LOWER DECK. GOOD LUCK!\n")
    print("You hurriedly make your way to the oxygen chamber.\n")
    print("Upon arrival, you check the status of the Oxygen panel.\n") 
    print("The Oxygen readings are lower than normal.\n")
    print("And There seems to be a strange noise coming from the machine.")
    print("\nchoose an option\n")

    # prompt user for choice
    correct_option = 4
    my_input = 99

    while my_input != correct_option:
        input_options("Turn oxygen generator off and back on again","Open toolbox",
            "Kick the oxygen machine to see if that fixes it","Open front panel")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_1") 

#   if we get this far then we've passed the first issue 
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou lean in closer to inspect, and you discover that some of the components are a bit loose...\n")
    print("\nwhat will you do?\n")

    # prompt user for choice
    correct_option = 3
    my_input = 99

    while my_input != correct_option:
        input_options("Check each component to ensure that it is secured correctly",
            "Pull all the loose components out and throw on the floor","Open toolbox",
            "Tie the panel door shut to decrease the noise")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()

        if my_input != correct_option:
            general_error("scenario_1") 

#   if we get this far then we've passed the second issue 
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou open your toolbox and look inside, there are several tools that may help...\n")
    print("Which tool will you use?\n")

    # prompt user for choice
    correct_option = 2
    my_input = 99

    while my_input != correct_option:
        input_options("The welder","The hose pipe","The comms card","The spanner")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_1") 

    print("\nYou select the hose pipe from the toolbox. You then switch off the oxygen generator")
    print("and disconnect the old hose pipe.\n")
    print("You notice that it is full of holes and it is coming apart.\n")
    print("You securely replace the old hose pipe with the new one and re-start the oxygen machine.\n")
    print("The Oxygen machine bursts into life and the oxygen levels start to rise dramatically...\n")

#   if we get this far then we've successfully resolved the issue 
    # <<<<<<< User game dialogue text here ... >>>>
    run_reward("scenario_1")    

#   if we get this far then we've successfully resolved the issue 
    scenario_1_complete = True

#***************************************************************************

def scenario_2():
#***************************************************************************
#   SCENARIO 2 - OXYGEN External issue
#***************************************************************************
    # <<<<<<< User game dialogue text here ... >>>>
    print("\n\nAlthough the oxygen panel is now working at an increased rate,")
    print("you notice that something is still wrong, and it wont work at full Capacity.")
    print("\nZED: OUR WORK IS NEVER DONE...\n")
    print("\nWhat will you do?\n")

    # prompt user for choice
    correct_option = 2
    my_input = 99

    while my_input != correct_option:
        input_options("Ignore problem and hope it fixes itself","Decide to check outside",
            "Open tool box","Call for help")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_2") 

    print("\nAs you've done all you can internally, you determine that there must be a problem externally.\n")
    print("You decide to take a space walk to investigate further...\n")
    print("You notice that there is damage to the ships hull, probably from a collision with something.\n")
    print("There is also a fine spray of gas leaking out from the ship... oxygen is escaping!\n")
    print("ZED: WELL THAT LOOKS LIKE A BIG PROBLEM...\n")
    print("\nWhat will you do?\n")

#   if we get this far then we've passed the first issue 
    # <<<<<<< User game dialogue text here ... >>>>
    # prompt user for choice
    correct_option = 4
    my_input = 99

    while my_input != correct_option:
        input_options("Push some rags into the hole to try to seal it","Call it a day",
            "Go back inside the ship for help","Open toolbox")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_2") 

#   if we get this far then we've passed the second issue 
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou open the toolbox and look inside... there are several tools they may help...\n")
    print("\nWhich tool will you select?\n")

    # prompt user for choice
    correct_option = 2
    my_input = 99

    while my_input != correct_option:
        input_options("Select hose pipe","Select welder","Select comms card","Select spanner")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_2") 

#   if we get this far then we've successfully resolved the issue 
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou grab a piece of steel plate floating around amongst the debris")
    print("and use the welder to seal it over the damaged area of the ship's hull.\n")
    print("The fix looks good ...\n")
    print("You then re-enter the ship and go to the Oxygen panel to test the system.\n")
    print("You switch on the Oxygen machine and it crackles into life - the oxygen pressure is nice and strong!\n")

    run_reward("scenario_2") 

def scenario_3():
#***************************************************************************
# SCENARIO 3 - COMMS Internal issue
#***************************************************************************
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou then hear an alarm coming from down the corridor\n")
    print("ZED: THE ALARM IS COMING FROM THE COMMUNICATION CENTRE.\n")
    print("You go to investigate ...\n") 
    print("Upon entering the COMMS ROOM, you see smoke coming from the COMMS panel\n")
    print("ZED: YOU KNOW WHAT THEY SAY, THERE IS NO SMOKE WITHOUT FIRE\n")
    print("What will you do?\n")

#   prompt user for choice
    correct_option = 3
    my_input = 99

    while my_input != correct_option:
        input_options("Throw water on comms panel","Run away!","Open comms panel",
            "See if the terminal catches fire")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_3") 

#   if we get this far then we've passed the first issue 
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou see the comms card has overheated and is starting to give off a burning smell.\n")
    print("To prevent a fire, you remove the comms card from the terminal.\n")
    print("The comms card looks beyond repair.\n")
    print("ZED: LETS NOT SET THE SHIP ON FIRE, IT MIGHT BE A BIT PROBLEMATIC...\n")

    print("\nWhat will you do?\n")

    # prompt user for choice
    correct_option = 1
    my_input = 99

    while my_input != correct_option:
        input_options("Open toolbox","Pour water on comms machine",
            "Put the comms card back","Quickly leave the room")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_3") 

#   if we get this far then we've passed the second issue 
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou open the toolbox and look inside ... ")
    print("There are several tools that may help...\n")
    print("\nWhich one will you choose?\n")
    
    correct_option = 3
    my_input = 99

    while my_input != correct_option:
    # prompt user for choice
        input_options("The hose pipe","The welder","The comms card","The spanner")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_3") 

#   if we get this far then we've successfully resolved the issue 
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou turn off the comms server, and check for additional damage.\n")
    print("Then you insert the new comms card.\n")
    print("You switch on the comms machine ... it bursts into life ...\n")

    run_reward("scenario_3")    

def scenario_4():
#***************************************************************************
#   SCENARIO 4 - COMMS External issue
#***************************************************************************
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou check the status of the COMMS panel\n")
    print("At first glance, everything seems to be working and intact, but the")
    print("strenght of the signal is very low.\n")
    print("ZED: THERE MUST BE A PROBLEM WITH THE TRANSMITTER FROM THE OUTSIDE!\n") 
    print("You decide to go and investigate... \n")
    print("You notice that the satellite dish has come loose, and it's hanging on the ship by a thread\n")
    print("\nWhat will you do?\n")

#   prompt user for choice
    correct_option = 2
    my_input = 99

    while my_input != correct_option:
        input_options("Go back inside the ship for help","Open toolbox",
            "Push the dish back into place and hope","Use ZED as a receiver")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_4") 

#   if we get this far then we've passed the first issue 
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou open the toolbox and look inside, there are several tools that may help...\n")
    print("\nWhat will you do?\n")

    correct_option = 4
    my_input = 99

    while my_input != correct_option:
        input_options("Select hose pipe","Select Welder","Select comms card","Select spanner")
#       my_input = (int(input("Enter 1 - 4: "))) # test / verify user input
        my_input = check_int()
        if my_input != correct_option:
            general_error("scenario_4") 

#   if we get this far then we've passed the second issue 
    # <<<<<<< User game dialogue text here ... >>>>
    print("\nYou push the satellite dish back into alignment and use the spanner to tighten up")
    print("the bolts to securely fix it into place.\n")
    print("You then re-enter the ship and go to the comms panel to test the system.\n")
    print("You switch on the comms machine and everything appears to be in working order!\n")
    print("not only is the oxygen stabalised, but you have also managed")
    print("to get communications up and running as well!")

    run_reward("scenario_4")    

#***************************************************************************
#
#   set up global variables
#
#***************************************************************************
oxygen_desc = ""
oxygen_fix = ""
oxygen_health = ""
comm_desc = ""
comm_health = ""
comm_fix = ""
sound_on = True
user_name = ""
user_health = 100
crew1_health = 0
crew2_health = 0
crew3_health = 0
crew4_health = 0
scenario_1_complete = False
scenario_2_complete = False
scenario_3_complete = False
scenario_4_complete = False
early_exit = False

#***************************************************************************
#
#   run the program
#
#***************************************************************************
#   set initial statuses for game and randomizer
set_initial_statuses()

#   get user / sound options
get_game_details()

#   display opening text / game scenario
opening_credits(user_name)

anykey_to_continue()    # temp pause - any key to continue

# scenario 1 goes here 
scenario_1()
print("\n\n")

# scenario 2 goes here 
scenario_2()
print("\n\n")

# scenario 3 goes here 
scenario_3()
print("\n\n")

# scenario 4 goes here 
scenario_4()
print("\n\n")

#   display closing text / thank you 
#   anykey_to_continue()    # temp pause - any key to continue
closing_credits()