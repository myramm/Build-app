label latinas_dialogue_shower:
    scene location_school_lockershowers_closeup
    show martinez b_towel f_angry zorder 1:
        xoffset -262
    show lopez b_towel f_angry zorder 2
    show player 57 zorder 0 at left
    with dissolve
    lopez "Hey! What are you doing in here?"
    show player 58
    player_name "Umm... Just trying to take a shower?"
    show player 59
    lopez "Listen, boy. This is our turf, so go take a walk elsewhere!"
    show martinez f_normal
    martinez "Wait, {b}Lopez{/b}!"
    martinez "Yo, I think this guy's the one people have been talking about!"
    show lopez f_angry_left
    lopez "What?! No way..."
    lopez "You telling me this guy's packing a {i}huge dick{/i}?"
    show lopez f_angry
    show martinez f_angry
    martinez "Alright boy! Show us what you got down there, and you can get in!"
    show player 60
    player_name "Uhh... I think I'll pass. I'll just shower at home then."
    show martinez b_towelgrab
    pause
    show player 61
    show lopez f_surprised_down
    show martinez b_towel a_hold_towel f_smirk_down
    with hpunch
    pause
    player_name "..."
    show player 62
    show martinez f_normal_right
    martinez "There you go!"
    show martinez f_smirk_down
    show lopez f_normal_down
    lopez "... That's what you call {i}big{/i}?"
    show martinez f_surprised_right
    martinez "Wha-"
    show player 63
    show martinez f_suspicious
    martinez "You soft?!"
    martinez "... He needs a little excitement..."
    show martinez f_eyeroll
    martinez "... Hmm..."
    show martinez f_normal_right
    martinez "... This should do the trick!"
    show lopez f_normal with None
    show martinez a_empty
    show martinez_body_parts a_towel_hold_towel_pull1 zorder 3
    with dissolve
    pause
    show player 64
    show lopez f_surprised_down_down b_toweldown a_surprised
    show martinez f_smirk_down
    show martinez_body_parts a_towel_hold_towel_pull2
    with hpunch
    pause
    show lopez f_angry_left a_down_cover1
    show martinez a_crossed
    hide martinez_body_parts
    with dissolve
    lopez "Oh my god, puta!"
    show lopez f_angry
    show martinez f_normal_right
    martinez "Chill, everyone's seen 'em at school already!"
    show martinez f_laugh
    martinez "Haha!"
    show martinez f_smirk_down
    show lopez f_surprised_down
    lopez "Yo, it's not doing anything!"
    show lopez f_normal_down
    show martinez f_eyeroll
    martinez "Maybe he's into guys?"
    show martinez f_angry
    show lopez a_down_pull1 with dissolve
    lopez "Here, I know what will work!"
    show martinez b_empty_towel
    show martinez_body_parts b_towelup zorder 0
    show lopez f_normal_down a_down_pull2
    with dissolve
    pause
    show martinez f_smirk_down2
    show lopez f_surprised_down
    with hpunch
    pause
    show player 65
    show martinez f_smirk_down
    player_name "... Oh... No..."
    pause
    show player 66 with hpunch
    show martinez f_surprised_down
    pause
    hide martinez_body_parts
    show martinez b_towel
    show lopez f_surprised_right a_down_cover2
    with dissolve
    show player 67
    lopez "Oh, shit!"
    lopez "{b}Annie{/b}'s coming!!"
    show lopez f_sorry
    show martinez f_sad_down a_cover with dissolve
    show player 68
    show old_annie 1 zorder 3 at Position (xpos=400)
    annie "..."
    show old_annie 3
    annie "What's going on here?!"
    show player 69
    show old_annie 1
    player_name "I was just trying to-"
    show player 68
    show old_annie 3
    annie "Expose yourself inappropriately?"
    show old_annie 4
    annie "AGAIN?!"
    show player 69
    show old_annie 6
    player_name "No, that's not-"
    show player 68
    show old_annie 5
    annie "I don't want to hear your pathetic excuses!"
    annie "My orders are to bring in repeated offenders to the office!"
    show old_annie 7
    annie "Come with me, NOW!!!"
    show old_annie 8f
    annie "... And you two, get out of here before I send you both to detention!!!"
    hide lopez
    hide martinez
    hide player
    hide old_annie
    with dissolve
    $ renpy.end_replay()
    return

label latinas_dialogue_leave:
    show player 57 at left
    show martinez b_towel f_angry zorder 1:
        xoffset -262
    show lopez b_towel f_angry zorder 2
    with dissolve
    lopez "Hey! You here to get us in trouble again?"
    show player 58 at left
    player_name "Umm... Just trying to take a shower?"
    show player 59 at left
    martinez "Get out of here, yo!"
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
