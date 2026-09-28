label button_ross_office_generic_pre_hscene:
    scene expression player.location.background_closeup
    show old_ross 11 at left
    show player 1f at right
    with dissolve
    ross "Well, hello there, {b}[firstname]{/b}."
    ross "Nice of you to visit me!"
    show old_ross 10
    show player 2f
    player_name "Hey, {b}Miss Ross{/b}."
    show old_ross 11
    show player 1f
    ross "What can I do for you?"
    return

label button_ross_office_generic_post_hscene:
    scene expression player.location.background_closeup
    show old_ross 10 at left
    show player 2f at right
    with dissolve
    player_name "Hey, {b}Miss Ross{/b}!"
    show player 1f
    show old_ross 27 with dissolve
    ross "{b}[firstname]{/b}! It's so good to see you!"
    show old_ross 13 with dissolve
    ross "... I hope you're here for another private lesson?"
    return

label ross_dialogue_office_private_lessons:
    show old_ross 12
    show player 2f
    player_name "Yeah, I'd love that!"
    show old_ross 13
    show player 1f
    ross "Mmm, hurry and lock the door!"
    show old_ross 12
    show player 2f
    player_name "O-okay..."
    return

label ross_dialogue_office_leave:
    scene expression player.location.background_closeup
    show old_ross 10 at left
    show player 2f at right
    player_name "Oh, I don't need anything."
    player_name "Sorry to bother you."
    show old_ross 11
    show player 1f
    ross "It's no bother, {b}[firstname]{/b}!"
    ross "Helping talented young artists is my specialty after all!"
    show old_ross 10
    show player 2f
    player_name "Heh, okay."
    player_name "I should get going..."
    show old_ross 11
    show player 1f
    ross "Aww, alright."
    ross "Bye, {b}[firstname]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
