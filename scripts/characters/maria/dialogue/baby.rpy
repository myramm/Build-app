label maria_button_baby:
    $ renpy.dynamic(local=flip if game.timer.is_evening() and
                                  L_maria_lounge.is_here(M_maria) else reset)

    show maria a_baby f_normal_down
    show anon at local with dissolve
    maria "So then the kid says, \"Silly old bear...\""
    maria "\"If we can't pull you out, we'll just have to push you back in.\""
    maria "But the rabbit didn't like the sound of that."
    maria "Not one bit!"
    maria "He ran inside and pushed as hard as he could on that fat old bear."
    maria "But it was no use."
    maria "He was good stuck and there was nothin' for it."
    maria "\"We'll just have to wait for you to get thin again...\" the kid says."

    menu maria_button_baby.choice:
        "What are you doing?":

            jump maria_button_baby.stories
        "I'll leave you be.":

            pass

    anon f_normal "I'll leave you be."
    maria f_normal "Be careful out there {b}[firstname]{/b}."
    anon "Will do."
    hide anon with dissolve
    return


label maria_button_baby.stories:
    anon f_normal "What are you doing?"
    maria f_normal "Oh, I'm just tellin' my favorite story from when I was little..."
    if M_maria.pregnancy.baby_gender == "boy":
        maria "He seems to like it."
    elif M_maria.pregnancy.baby_gender == "girl":
        maria "She seems to like it."
    else:
        maria "They seem to like it."
    anon "Aww, that's really sweet, {b}Maria{/b}!"
    maria "You're welcome to stay and listen, if you want."
    show maria f_normal_down
    jump maria_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
