label spin_bottle_minigame_kiss_mc_roxxy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show old_roxxy front sitting 1 at Position (xoffset=3)
    show player car 2b zorder 1 at Position (xoffset=-3)
    show player_arms car 1 zorder 2 at Position (xoffset=-3)
    with dissolve
    pause
    show player front sitting 7 at Position (xoffset=-3)
    show player_shadow front sitting 1 zorder 0
    show player_arms front sitting 3 at Position (xoffset=3-3)
    show old_roxxy front sitting 3b at Position (xoffset=3)
    show old_roxxy_arm front sitting 1 at Position (xoffset=3)
    with dissolve
    roxxy "Mmm."
    player_name "..."
    show player front sitting 7b at Position (xoffset=-3)
    show old_roxxy front sitting 3 at Position (xoffset=3)
    pause
    show player front sitting 7 at Position (xoffset=-3)
    show old_roxxy front sitting 3b at Position (xoffset=3)
    if randomizer() < 33:
        missy "They're so cute together, aren't they {b}Becca{/b}?"
        becca "..."
    elif randomizer() < 66:
        roxxy "He's like, the best kisser..."
        missy "I'm so jelly right now."
        becca "..."
    else:
        becca "{b}Roxxy{/b}'s really skilled with her tongue..."
        missy "Yeah, but so is {b}[firstname]{/b}!"
        becca "..."
    show player front sitting 7b at Position (xoffset=-3)
    show old_roxxy front sitting 3 at Position (xoffset=3)
    pause
    hide player
    hide old_roxxy
    hide old_roxxy_arm
    hide player_arms
    hide player_shadow
    with dissolve
    return

label spin_bottle_minigame_kiss_mc_becca:
    if randomizer() > 50:
        scene expression "backgrounds/location_beach_fire_kiss.jpg"
        show old_becca front sitting 1
        show player car 2b zorder 1
        show player_arms car 1 zorder 2
        with dissolve
        pause
        show player front sitting 7b
        show player_shadow front sitting 1 zorder 0
        show player_arms front sitting 3
        show old_becca front sitting 3
        with dissolve
        becca "Mmm."
        player_name "..."
        show player front sitting 7
        show old_becca front sitting 3b
        pause
        show player front sitting 7b
        show old_becca front sitting 3
        if randomizer() < 33:
            roxxy "Yeah, that's it..."
            roxxy "Play with her nipples!"
            missy "Hehe, look how turned on she is!"
        elif randomizer() < 66:
            missy "I'm sorry you have to kiss that ugly freckle faced ginger, {b}[firstname]{/b}..."
            roxxy "Shut up, {b}Missy{/b}..."
        else:
            roxxy "This is really hot!"
        show player front sitting 7
        show old_becca front sitting 3b
        if randomizer() < 50:
            roxxy "C'mon {b}Becca{/b}, use more tongue!"
            becca "..."
        else:
            missy "Bleh, {b}Becca{/b} is a boring kisser."
            missy "Just wait 'til it's my turn, {b}[firstname]{/b}!"
        show player front sitting 7b
        show old_becca front sitting 3
    else:

        scene expression "backgrounds/location_beach_fire_kiss.jpg"
        show old_becca front sitting 1
        show player car 2b zorder 1
        show player_arms car 1 zorder 2
        with dissolve
        pause
        show player_shadow front sitting 1 zorder 0
        show player front sitting 7
        show player_arms front sitting 4
        show old_becca front sitting 3b
        with dissolve
        if randomizer() < 33:
            becca "Ngghhh!"
        else:
            becca "Mmm."
            player_name "..."
        show player front sitting 7b
        show player_arms front sitting 4d
        show old_becca front sitting 3
        pause
        show player front sitting 7
        show player_arms front sitting 4
        show old_becca front sitting 3b
        if randomizer() < 33:
            roxxy "Yeah, that's it..."
            roxxy "Play with her nipples!"
            missy "Hehe, look how turned on she is!"
        elif randomizer() < 66:
            missy "I'm sorry you have to kiss that ugly freckle faced ginger, {b}[firstname]{/b}..."
            roxxy "Shut up, {b}Missy{/b}..."
        else:
            roxxy "This is really hot!"
        show player front sitting 7b
        show player_arms front sitting 4d
        show old_becca front sitting 3
        if randomizer() < 50:
            roxxy "C'mon {b}Becca{/b}, use more tongue!"
            becca "..."
        else:
            missy "Bleh, {b}Becca{/b} is a boring kisser."
            missy "Just wait 'til it's my turn, {b}[firstname]{/b}!"
        show player front sitting 7
        show player_arms front sitting 4
        show old_becca front sitting 3b
    pause
    hide player
    hide player_arms
    hide player_shadow
    hide old_becca
    with dissolve
    return

label spin_bottle_minigame_kiss_mc_missy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show old_missy front sitting 1
    show player car 2b zorder 1 at Position (xoffset=-7)
    show player_arms car 1 zorder 2 at Position (xoffset=-7)
    pause
    show player_shadow front sitting 1 zorder 0
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show old_missy front sitting 3b
    show old_missy_arm front sitting 1 zorder 3
    missy "Mmm."
    player_name "..."
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show old_missy front sitting 3
    pause
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show old_missy front sitting 3b
    if randomizer() < 33:
        roxxy "Yeah, squeeze those tits, {b}[firstname]{/b}!"
        becca "There's barely anything there to squeeze..."
        roxxy "Shut up, {b}Becca{/b}."
    if randomizer() < 66:
        becca "God, she's a sloppy kisser!"
        becca "Just what in the hell is she trying to do with her tongue, anyways?!"
        roxxy "I know, right?"
        roxxy "Somebody needs to teach that girl how to French..."
    else:
        roxxy "Slow down, {b}Missy{/b}!"
        roxxy "She's so freaking impatient..."
        becca "Yeah, I think she just needs to get laid."
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show old_missy front sitting 3
    pause
    hide player
    hide player_shadow
    hide player_arms
    hide old_missy
    hide old_missy_arm
    with dissolve
    return

label spin_bottle_minigame_kiss_becca_missy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show old_becca front sitting 1f at Position (xoffset=-4)
    show old_missy front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show old_becca front sitting 3bf at Position (xoffset=-4)
    show old_missy front sitting 3 at Position (xoffset=4)
    show old_missy_arm front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show old_becca front sitting 3f at Position (xoffset=-4)
    show old_missy front sitting 3b at Position (xoffset=4)
    if randomizer() < 33:
        roxxy "Isn't this hot, {b}[firstname]{/b}?"
        player_name "Y-yeah..."
    if randomizer() < 66:
        roxxy "Mmm, c'mon {b}Missy{/b}..."
        roxxy "You gotta be assertive with {b}Becca{/b}!"
        roxxy "She likes it rough!"
    else:
        becca "Mmm."
    show old_becca front sitting 3bf at Position (xoffset=-4)
    show old_missy front sitting 3 at Position (xoffset=4)
    if randomizer() < 33:
        roxxy "{b}Becca{/b} pretends that she doesn't like it but look how hard her nipples are!"
        player_name "..."
    if randomizer() < 66:
        player_name "..."
    else:
        roxxy "Oh, it sounds like {b}Missy{/b}'s starting to get the hang of it!"
    show old_becca front sitting 3f at Position (xoffset=-4)
    show old_missy front sitting 3b at Position (xoffset=4)
    pause
    show old_becca front sitting 3bf at Position (xoffset=-4)
    show old_missy front sitting 3 at Position (xoffset=4)
    if randomizer() < 50:
        player_name "..."
        roxxy "Is this making you hard, {b}[firstname]{/b}?"
        player_name "Y-yes..."
        roxxy "Hehehe!"
    show old_becca front sitting 3f at Position (xoffset=-4)
    show old_missy front sitting 3b at Position (xoffset=4)
    pause
    hide old_missy
    hide old_becca
    hide old_missy_arm
    with dissolve
    return

label spin_bottle_minigame_kiss_roxxy_becca:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show old_roxxy front sitting 1 at Position (xoffset=5)
    show old_becca front sitting 1f
    with dissolve
    pause
    show old_roxxy front sitting 3 at Position (xoffset=5)
    show old_roxxy_arm front sitting 2d
    show old_becca front sitting 3bf
    if randomizer() < 33:
        becca "Ngghhh..."
    if randomizer() < 66:
        missy "Hehe, I love watching {b}Roxxy{/b} manhandle {b}Becca{/b}..."
        missy "'Cause she's usually such a stuck up bitch, you know?"
        player_name "Y-yeah."
        missy "... But look at her now."
        missy "Moaning like a dirty little whore."
        player_name "..."
    else:
        becca "Mmm."
    show old_roxxy front sitting 3b at Position (xoffset=5)
    show old_roxxy_arm front sitting 2c
    show old_becca front sitting 3f
    if randomizer() < 50:
        missy "Damn!"
        missy "Look at {b}Becca{/b} squirming!"
    else:
        missy "Doesn't {b}Roxxy{/b} taste good, {b}Becca{/b}?"
        becca "Mmmhmm..."
        missy "Hehe."
    show old_roxxy front sitting 3 at Position (xoffset=5)
    show old_roxxy_arm front sitting 2d
    show old_becca front sitting 3bf
    if randomizer() < 50:
        player_name "..."
        missy "{b}Roxxy{/b} really knows how to push her buttons."
    show old_roxxy front sitting 3b at Position (xoffset=5)
    show old_roxxy_arm front sitting 2c
    show old_becca front sitting 3f
    pause
    hide old_roxxy
    hide old_roxxy_arm
    hide old_becca
    with dissolve
    return

label spin_bottle_minigame_kiss_roxxy_missy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show old_roxxy front sitting 1 at Position (xoffset=2)
    show old_missy front sitting 1f at Position (xoffset=-2)
    with dissolve
    pause
    show old_roxxy front sitting 3b at Position (xoffset=2)
    show old_missy front sitting 3f at Position (xoffset=-2)
    show old_missy_arm front sitting 1f at Position (xoffset=-2)
    show old_roxxy_arm front sitting 1 at Position (xoffset=2)
    with dissolve
    if randomizer() < 50:
        missy "Ngghhh!!!"
    show old_roxxy front sitting 3 at Position (xoffset=2)
    show old_missy front sitting 3bf at Position (xoffset=-2)
    if randomizer() < 50:
        becca "Yeah, pinch that skank's nipples!"
        becca "Hahaha!"
    else:
        becca "Mmm, this {b}GoldSchwagger{/b} is so delicious!"
        becca "You sure you don't want some, {b}[firstname]{/b}?"
        player_name "Heh, nah that's alright."
        player_name "Just beer for me."
        becca "Booo!!"
    show old_roxxy front sitting 3b at Position (xoffset=2)
    show old_missy front sitting 3f at Position (xoffset=-2)
    if randomizer() < 50:
        becca "Ugh, look at {b}Missy{/b}'s technique..."
        becca "... So sloppy."
        player_name "Maybe you two should practice during the week?"
        becca "We practice together all the time, she just doesn-"
        becca "!!!"
        becca "I mean..."
        becca "We don't..."
        becca "That's just the booze talking, {b}[firstname]{/b}!"
        player_name "Heh, alright."
    show old_roxxy front sitting 3 at Position (xoffset=2)
    show old_missy front sitting 3bf at Position (xoffset=-2)
    pause
    hide old_missy
    hide old_missy_arm
    hide old_roxxy_arm
    hide old_roxxy
    with dissolve
    return

label spin_bottle_minigame_last_spin:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 1 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show old_missy sitting 1 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    roxxy "Mmm..."
    show old_roxxy sitting 3
    roxxy "Okay, last spin."
    return

label spin_bottle_minigame_final_spin:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 1 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show old_missy sitting 1 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    roxxy "Mmm..."
    show old_roxxy sitting 3
    roxxy "Okay, last spin."
    roxxy "Winner goes to the changing room with {b}[firstname]{/b}!"
    show old_roxxy sitting 2
    show old_becca sitting 2
    show old_missy sitting 2
    show player_sitting 3b
    pause
    show player_sitting 3
    pause
    show player_sitting 5
    pause
    show player_sitting 11
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
