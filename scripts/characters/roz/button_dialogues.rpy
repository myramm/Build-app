label roz_dialogue_basement_priya:
    scene hospital_desk
    show old_roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 10f at right
    player_name "I wanted to ask you about the basement."
    show player 5f
    show old_roz 2
    roz "It's restricted."
    show old_roz 1
    show player 12f
    player_name "Y-yeah, I know..."
    player_name "... But I was hoping, maybe, you could tell me who has access?"
    show player 5f
    show old_roz 2
    roz "No, that's restricted."
    show old_roz 1
    show player 12f
    player_name "... But I just need to-"
    show player 5f
    show old_roz 2
    roz "Restricted."
    show old_roz 1
    show player 35f
    player_name "Could you like, page one of the doctors working down there?"
    player_name "I need to speak with {b}Doctor Singh{/b}."
    show player 90f
    show old_roz 2
    roz "I could."
    show old_roz 1
    pause
    player_name "..."
    show player 10f
    player_name "Would you?"
    show player 5f
    show old_roz 2
    roz "No."
    show old_roz 1
    show player 15f
    player_name "Look, I really need to speak with him."
    player_name "It's very important!"
    show player 16f
    show old_roz 2
    roz "Oh, I didn't realize it was important..."
    show old_roz 1
    pause
    show player 10f
    player_name "So you'll do it?"
    show player 5f
    show old_roz 2
    roz "... No."
    show old_roz 1
    show player 15f
    player_name "Then why did you?!"
    show player 16f
    show old_roz 2
    roz "It's restricted."
    show old_roz 1
    show player 37f with dissolve
    player_name "{i}*Sigh*{/i}"
    show player 38f with dissolve
    player_name "Is there something I can do to change your mind?"
    show player 90f with dissolve
    show old_roz 2
    roz "Restrict-"
    show old_roz 1
    pause
    show old_roz 2
    roz "Oh."
    roz "Hmm, I doubt it."
    show old_roz 1
    pause
    show player 25f
    player_name "I'll do anything!"
    show player 24f
    show old_roz 2
    roz "Anything?"
    show old_roz 1
    show player 25f
    player_name "Literally. Anything."
    show player 24f
    roz "Hmm."
    show old_roz 2
    roz "You any good with cameras?"
    show old_roz 1
    show player 12f
    player_name "Cameras?"
    player_name "Yeah, I guess."
    show player 5f
    show old_roz 2
    roz "I got this new fangled one from the store and the damn thing won't work."
    show old_roz 1
    show player 14f
    player_name "I could probably figure it out!"
    show player 13f
    roz "Hmm."
    show old_roz 2
    roz "Follow me then."
    hide old_roz
    hide xtra 35
    with dissolve
    pause
    show player 4f
    player_name "( Wow, she's gonna take me down to the {b}basement{/b} just for fixing her camera? )"
    player_name "( How about that, I finally caught a break. )"
    hide player with dissolve
    return

label roz_dialogue_basement:
    scene hospital_desk
    show old_roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 10f at right
    player_name "I wanted to ask you about the basement."
    show player 5f
    show old_roz 2
    roz "It's restricted."
    show old_roz 1
    show player 12f
    player_name "Y-yeah, I know..."
    player_name "... But I was hoping, maybe, you could tell me who has access?"
    show player 5f
    show old_roz 2
    roz "No, that's restricted."
    show old_roz 1
    show player 12f
    player_name "... But I just need to-"
    show player 5f
    show old_roz 2
    roz "Restricted."
    return


label roz_dialogue_intro:
    scene hospital_desk
    show old_roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 14f at right
    with dissolve
    player_name "Hi!"
    show player 13f
    show old_roz 2
    roz "Yes?"
    roz "What can I do for you?"
    show old_roz 1
    return

label roz_dialogue_1st_floor:
    show player 12f
    player_name "What can I find on the 1st floor?"
    show player 5f
    roz "..."
    show old_roz 2
    roz "It's the lobby."
    show old_roz 1
    show player 10f
    player_name "Oh... Is there anything else?"
    show player 5f
    show old_roz 3 with dissolve
    roz "Do you see anything else?"
    show old_roz 1 with dissolve
    show player 24f
    player_name "I guess not..."
    show player 25f
    show old_roz 2
    roz "Anything else I can do?"
    show old_roz 1
    show player 13f
    return

label roz_dialogue_2nd_floor:
    show player 12f
    player_name "What can I find on the 2nd floor?"
    show player 5f
    show old_roz 2
    roz "We have sick rooms, and a storage room on the 2nd floor."
    show old_roz 1
    show player 12f
    player_name "Oh. I see."
    show player 5f
    show old_roz 2
    roz "Anything else I can do?"
    show old_roz 1
    show player 13f
    return

label roz_dialogue_3rd_floor:
    show player 12f
    player_name "What can I find on the 3rd floor?"
    show player 5f
    show old_roz 2
    roz "That's our maternity floor, it's where you'll find our recovery rooms."
    show old_roz 1
    show player 12f
    player_name "Ok, thanks."
    show player 5f
    show old_roz 2
    roz "Anything else I can do?"
    show old_roz 1
    show player 13f
    return

label roz_dialogue_schedule:
    show player 12f
    player_name "Is there always someone at the reception?"
    show player 5f
    show old_roz 2
    roz "Yes."
    roz "I'm always here."
    show old_roz 1
    show player 12f
    player_name "You never leave your desk?"
    show player 5f
    show old_roz 2
    roz "Why do you ask?"
    show old_roz 1
    show player 10f
    player_name "Err... Just wondering?"
    show player 5f
    show old_roz 2
    roz "I only leave my desk in case of an emergency."
    show player 11f
    roz "If I don't get a {b}phone call{/b}, I don't leave."
    show old_roz 1 with dissolve
    show player 14f
    player_name "Oh. I see."
    show player 13f
    show old_roz 2
    roz "Anything else I can do?"
    show old_roz 1
    return

label roz_dialogue_ancestory:
    show player 14f
    show old_roz 1
    player_name "{b}Roz{/b}! I need to ask you something."
    show player 11f
    show old_roz 2
    roz "Hmm, yes?"
    show old_roz 1
    show player 10f
    player_name "I'm trying to find the gravesite of someone who died in this town, a long time ago."
    show player 29f
    player_name "I think he was some kind of shipwright."
    player_name "Do you have any ideas on the best way to go about finding it?"
    show player 3f
    show old_roz 2
    roz "I might have an idea or two."
    show old_roz 1
    roz "..."
    show player 11f
    player_name "..."
    show player 12f
    player_name "Could you tell me?"
    show player 11f
    show old_roz 2
    roz "I probably could."
    show old_roz 1
    roz "..."
    show player 16f
    player_name "..."
    show player 30f
    player_name "{i}*Sigh*{/i} Will you please tell me?"
    show player 16f
    show old_roz 2
    roz "What's this fella's name?"
    show player 29f
    show old_roz 1
    player_name "Well, that's the problem... I don't know his name."
    show player 11f
    show old_roz 2
    roz "Hmm..."
    roz "... Well, that makes things difficult, doesn't it?"
    show player 25f
    show old_roz 1
    player_name "... Yeah."

    show player 24f
    show old_roz 2
    roz "I suppose It's possible you could {b}find him in the old obituary records{/b}."
    show player 11f
    roz "I seem to recall more than a few folk had their professions listed in there."
    show player 10f
    show old_roz 1
    player_name "Really?!"
    player_name "Well, that sounds promising!"
    show player 11f
    show old_roz 2
    roz "Problem is, it's gonna be a big hassle... me diggin' that old thing up."
    show player 29f
    show old_roz 1
    player_name "Oh?"
    show player 3f
    show old_roz 2
    roz "Maybe you could do something to make it worth my while?"
    show player 29f
    show old_roz 1
    player_name "O-of course!"
    show player 2f
    player_name "You let me take a look at those {b}records{/b} and I'll do anything you want!"
    show player 1f
    show old_roz 2
    roz "Hmm, anything?"
    show player 2f
    show old_roz 1
    player_name "Anything!"
    show player 1f
    roz "..."
    show old_roz 2
    roz "Alright, I tell ya what..."
    roz "... {b}Take this pass key up to the 2nd floor storage{/b}."
    roz "You'll find {b}an ugly box sitting there on the shelf{/b}, stands out like a sore thumb, you can't miss it."
    show player 2f
    show old_roz 1
    player_name "Ugly box, got it."
    show player 1f
    show old_roz 2
    roz "You go {b}get me that box and bring it back here{/b}, while I dig up those records."
    show player 2f
    show old_roz 1
    player_name "That sounds easy enough!"
    player_name "I'll be back in a flash!"
    hide player with dissolve

    show old_roz 2
    roz "Heh, sure you will kid. Sure you will."
    return

label roz_dialogue_go_on_break:
    show player 14f
    show old_roz 1
    player_name "I was wondering if you wanted to... Ya know, take your break?"
    show player 13f
    show old_roz 2
    roz "Ahh..."
    roz "Can't get enough of ole {b}Roz{/b}, eh kiddo?"
    show old_roz 1
    player_name "..."
    show old_roz 2
    roz "Don't you worry, message received."
    roz "You head on up to storage and I'll be along shortly..."
    roz "... Just need a moment to freshen up."
    show old_roz 1
    player_name "..."
    show player 14f
    player_name "S-sure, I'll be up there waiting."
    show player 13f
    hide player with dissolve
    show old_roz 2
    roz "That's a good boy..."
    return

label roz_dialogue_nothing:
    show player 14f
    player_name "No, I think that's all!"
    show player 13f
    show old_roz 2
    roz "Bye."
    return

label roz_phone_prompt:
    scene expression player.location.background_blur
    show player 13f with dissolve
    player_name "( I can't convince her to leave from here. )"
    player_name "( Maybe I can get someone to call her on the intercom? )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
