print('''You are a logger in the woods and you are cutting down a tree when all of the suddenyou see some bright lights and blown on your ass. You hear some strange voices coming from behind you, they do not sound human.''')
firstchoice =raw_input("do you want to -run- or -investigate-")
if(firstchoice =="investigate"):
    print("you get up and decide you want to investigate. You start to walk over to where you see somthing to look like a long lizzard tail coming from behind a tree. you go and check it out and an alien rips off you face. your dead")
elif(firstchoice =="run"):
	print("you run away because you know what was behind you was not friendly. You run far and and for a long time. You run up on a cabin. You find a wooden door, its locked. You run around the back to see if there is a back, there is, but its locked too. You find a shed and its open. You go and look for tools to open the door and you find an axe")
	secondchoice =raw_input("how do you open the door?")
	while(secondchoice != "use axe"):
		print("dint work, try again")
        secondchoice =raw_input("HINT: what chops wood?")
    if(secondchoice == "use axe"):
        print("Good. The axe knocked down the door. You run inside and shut what is left of the door but since you broke it, you need to find something to barricade it with but you are not sure if the creature knows where you are.")
        thirdchoice =raw_input("-barricade door- or -investigate the cabin-")
        if(thirdchoice =="investigate the cabin"):
            print("you leave the door and try to go see if there is anyone in the house or anything you can use to help you. You go down into the basment but you hear the front door upstairs open. there is no other way out of the basement so your trapt. So an alien comes into the basement and rips off your face.")
        elif(thirdchoice =="barricade door"):
            print("you find a dresser to put in front of the door to close it. You here things start to sound like they are communicating and getting close. You go and look around the house and then go into the basement where there is a shotgun the owner left in there. there is also a radio.")
     	    fourthchoice =raw_input("-call for help- or -load gun and wait-")
     	    if(fourthchoice =="call for help"):
     	        print("you grab the radio and call to see if anybody can here you and help. The radio transmission comes accross as static. The aliens intercepted the call and know you are in the basement and helpless. they call for backup from the ufo and get more of them. They break a window and you dont have enough bullets to stop all of them. They rip your face off and your dead.")
     	    elif(fourthchoice =="load gun and wait"):
     	        print("you load up the gun and wait for the aliens to come. Two of these green lizard looking things come down into the basement. you have a choice to shoot one or the other because you only have one bullet.")
     	        fifthchoice =raw_input("-shoot first- or -shoot second-")
     	        if(fifthchoice =="shoot second"):
     	        	print("the second one dies but the other one still comes and rips your face off.")
     	        elif(fifthchoice =="The first one was carrying a fuel cell for the ship and the bullet hit the fuel cell and caused it to explode. Both the aliens are dead and the you are able to escape and notify the police there are ETs crawling around all over the place anf=d then after that it is War of the Worlds part II. The end.")

