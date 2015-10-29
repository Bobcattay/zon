#name of story will be changed at a later time, as well as city name. I do not care for Zon at all,
#however that was all I could think of at the time. Is Zyra a good second main name? 

y_name = input("Hello there, young one. What is your name?").capitalize()
y_gen = input("What is your gender?").lower()
#this will be the main character's(the reader) name throughout the story

print ("""
    Welcome,""",y_name,""". You may not remember me, I'm Hrothgar, your friendly apothecary here.
You don't remember where you are, do you? Well, let me tell you, but first you better run. That man there outside my shop?
Yeah, he's not the kind of guy you'd typically have tea with. Oh, you also may have stolen his satchel of money. That means run, kid!
""")

print ("""
    You are running down the streets of Zon, making your way to the woods. You are almost out of breath, your chest heaving from the effort
it took to run away from those scoundrels. The money weighs down as if this money itself was the guilt that you carry with you. Even if this
money wasn’t for you, it’s hard to steal, it’s not right. But Zyra needs this money for her family. She needs to survive, that's what's important.
A few shillings won't be missed by a nobleman of such wealth.

    You reach the corner, stopping to regain some strength. To your right you see some police, but to your left, the nobleman, Sir Hersley
himself. You have to act quick.
""")

fr_turn = input("Will you turn left, towards Sir Hersley? Or right, to the cops?").lower()#variable for first turn, this will be the beginning of your story,
#it will sort of decide your fate, though you could go on various paths that could result in a similar or the same ending of the main story. 

if fr_turn == 'left':
    print ("\nSir Hersley it is. With a deep inhale of last hope, you sprint towards what seems like a bad decision.")
    print ("""
Without hesitation, you turn to your left and face this beast of a man. He seemed to loom over you like a monster, his face an ashen color of peach. Something seems off about this man, other than the fact that he is no longer angry. He almost seems like a ghost, an empty shell of himself. But how can than be when just a moment ago he was seething with anger and full of energy to chase you? 
You notice something big scuttling across the street behind Hersley. An elephant? But surely elephants don’t move with such rigid movements, even if mice were racing about it’s feet. It seems like a man trying to get your attention.

You are able to pass the now fainting Sir Hersley, making your way towards the elephant man. As you get closer, you realize that it is indeed a man, and not just any man, but Hrothgar from his apothecary shop! He is carrying a vial of bluish liquid, holding it away from his bulging body, which would consider his obscure movements. You pause in front of him, taking his old man-beardedness in. 

Through puffs of air, Hrothgar is able to tell you what’s going on.
“I… Poisoned… Him… He’s going… To die! “
“Oh… So what do I do now then?”
“Get those coins… To the woods!” 
 
The cops are now coming over to the ailing Sir Hersley, looking around for someone who may have done this to him.

“I’ll distract them, just go!” Yells the elephantine man, hobbling towards the officers. Will you run to the woods, or help Hrothgar get out of this mess he created?
""")

elif fr_turn == 'right':
    print ("\nWell, maybe with a shilling or two you can make it past the cops...")
    print ("""
You make a run for the police, careful to look not too crazy. You slow to a stop as you notice that they are busy with some kid who got himself stuck in the
bars of a gate. As one police is trying to pull the kid out, the other is in the front pushing. The poor fool is whimpering and crying, unable to do anything about the situation.

You are able to sneak past the cops without a problem. But then you notice another problem- the sheriff is walking right up to you.
Unfortunately there is no where to go, but lucky for you, Sir Hersley got stuck behind some horse traffic. 

“Hello there, good fellow. What is your name?” 
You respond with, “Hi there, I’m """,y_name,""". 
“I see that you have a nobleman after you. I’m going to have to take you in.”
“Well, you see, kind sir, I was hoping with a few shillings you would look the other way?”
“How much do you have to offer?”

You open up the coin purse and think about the options. How much are you willing to give to get away from that crazy man chasing you? You have thirty shillings.""")
