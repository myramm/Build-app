label maria_button_sex:
    show maria a_shy f_sexy with None
    show tony b_casual f_smirk behind maria:
        flip
        xoffset 25
    show anon f_flirt behind maria:
        xoffset -115
    with dissolve
    tony "Hey, the kid's here."

    tony "You ready to get started, darlin'?"

    maria "Tentu saja!"


    if M_tony.watches:
        tony "Tonight's gonna be the night, I can feel it!"

        show tony a_hold_mc_sides
        show anon o_tony_hand f_shy
        with dissolve
        tony f_normal_right "Right, champ?"

        anon "Y-yeah, definitely!"

        tony f_smirk "What do you think, darlin'?"

        show maria a_undress1 with dissolve
        show tony f_normal_down
        show anon f_flirt_low
        pause
        show maria b_lingerie_boob_bounce o_idle
        show tony o_casual_boner
        show anon o_boner
        with dissolve
        pause
        show maria b_lingerie_undress_bottom with dissolve:
            offset (50, 0)
        pause
        show maria b_naked f_sexy_lipbite_down a_idle
        show tony a_idle
        with dissolve
        tony @ f_normal_right "Heh, I think she agrees."

        show anon o_empty a_surprised
        show maria f_normal_down b_naked_bending a_idle:
            xoffset -115
        with dissolve
        pause .3
        show tony with slowdissolve:
            unflip
            xoffset 100
        pause
        show anon b_shirt od_dick3 -a_surprised
        show maria a_remove2
        with dissolve
        show anon od_dick4 with dissolve
        pause
        show anon od_empty
        show maria a_jerk f_normal_up
        with dissolve
        maria "Anda siap?"

        anon "Ya, Bu."

        show anon b_naked_changing3 od_naked_dick3
        show maria b_naked f_sexy_lipbite_down a_idle
        with dissolve
        pause
        show tony f_laugh a_frustrated
        show anon b_empty od_empty:
            xoffset 85
            yoffset 25
        show maria b_naked_pulling_mc f_sexy behind anon:
            xoffset 0
        with dissolve
        tony "Man, I have never seen her so aggressive before..."

        hide maria
        hide anon
        show tony:
            flip
            xoffset 450
        with {'master': dissolve}
        tony f_smirk a_idle "... Heh, you've really awoken somethin' here, champ!"

    else:
        tony f_sad "Well, I'll let you guys get to it then..."

        maria f_sad "Sorry, honey."

        tony "Tidak apa-apa."

        show tony with dissolve:
            unflip
            xoffset -300
        tony @ a_frustrated "Try and give her a couple orgasms before you blow your load, eh?"

        tony "It increases the odds of conception."

        anon "Y-ya, oke."

        tony "Oh, and don't forget the visualization thing we talked about!"

        show maria f_confused with dissolve:
            offset (50, 0)
        maria "Visualization thing?"

        maria "Apa-"

        show tony with {'master': dissolve}:
            flip
            xoffset 100
        tony "Don't worry about it, darlin'."

        hide tony
        show maria b_lingerie_kiss_tony
        with dissolve
        pause
        show tony b_casual f_sad behind maria:
            flip
            xoffset 100
        show maria b_lingerie f_sad a_idle
        with dissolve
        tony "Just enjoy yourself, eh?"

        show tony with {'master': dissolve}:
            unflip
            xoffset -300
        tony @ a_point "Fuck her good, champ."

        hide tony with dissolve
        maria f_shy "Should we get started?"

        anon f_flirt "Ya, Bu."

        show maria a_undress1 with dissolve
        show anon f_flirt_low
        pause
        show maria b_lingerie_boob_bounce o_idle with dissolve
        pause
        show maria b_lingerie_undress_bottom
        with dissolve
        pause
        show maria b_naked_shy2 f_sexy with dissolve
        maria "Mm, I've been thinking about that dick all day..."

        show anon a_surprised o_empty behind maria
        show maria f_normal_down b_naked_bending a_idle:
            xoffset -115
        with dissolve
        pause
        show anon b_shirt od_dick3 -a_surprised
        show maria a_remove2
        with dissolve
        show anon od_dick4
        pause
        show anon od_empty
        show maria a_jerk
        with dissolve
        maria "Anda siap?"

        anon "Ya, Bu."

        show anon b_naked_changing3 od_naked_dick3
        show maria b_naked f_sexy_lipbite_down a_idle
        with dissolve
        pause
        show anon b_empty od_empty:
            xoffset 85
            yoffset 25
        show maria b_naked_pulling_mc f_sexy behind anon:
            xoffset 0
        with dissolve
        pause

    call scene_maria_sex_storage.repeat (M_tony.watches)
    $ unlock_scene('maria', '01_unlocked', variant=M_tony.watches)

    if M_tony.watches:
        $ renpy.dynamic(inside=_return == 'inside', plus=_return == 'plus')

        call maria_button_stage
        hide maria
        show tony:
            xoffset -200

        if plus:
            call maria_button_sex.plus
        else:
            call maria_button_sex.tony

    return 'afterglow'


label maria_button_sex.plus:
    show expression background(512, 440, 2.5, l=L_pizzeria_kitchen) as stage
    show tony a_hips b_naked_shirt o_dick1
    show anon
    with fade
    tony "Hey, ya done real good in there, champ!"

    tony "She's gonna be seein' stars for a while after the number we just did on her."

    anon "Do you think I got her pregnant?"

    tony "Of course ya did!"

    tony "Did you see the orgasm we just gave her?"

    anon "Y-ya."

    tony "And with how deep you buried that thing in her, there ain't no doubt in my mind."

    tony "C'mere you!"

    hide anon
    show tony a_scrub f_normal_down
    with {'master': dissolve}
    anon "!!!"
    tony @ f_laugh "Hehehe!"

    show anon f_surprised_low a_rub:
        xoffset -50
    show tony a_frustrated f_normal
    with {'master': dissolve}
    tony "Now you go on and get home, eh?"

    show tony a_hips
    show anon f_worried

    if M_anon.finished_state(S_ano27_done):
        show anon f_worried_surprised
        with {'master': dissolve}
        tony "Say hi to that pretty mother of yours for me."

        anon f_worried "She's not-"

        show anon f_tired

    show anon a_sides
    with {'master': dissolve}
    anon "Y-ya, oke."

    anon f_shy "Later, {b}Tony{/b}."

    hide anon with dissolve
    return


label maria_button_sex.tony:
    show tony b_casual f_suspicious
    if inside:
        show anon
    else:
        show anon f_worried
    with fade
    if inside:
        tony "You up for it, champ?!"

        anon "Y-yeah, I guess... If you're sure that's what you want?"

        tony f_smirk "You kiddin'?!"

    else:
        anon "I'm sorry, {b}Tony{/b}."

        tony "Ahh, tidak apa-apa, jagoan."

    hide anon
    show tony a_scrub f_normal_down
    with dissolve
    if inside:
        tony "I'll take as many kids as you're willin' to give me!"

        anon "hehe!"

        tony "The more the merrier!"

    else:
        tony "Just don't make a habit of it, yeah?"

        anon "Hehe, I won't!"

    show anon f_normal a_rub:
        xoffset -50
    show tony a_frustrated f_normal
    with dissolve
    anon "I guess I'll see you both tomorrow then?"

    tony a_idle "You betcha!"

    maria "Sampai jumpa, {b}[firstname]{/b}."

    if inside:
        show anon f_flirt a_wave with dissolve
        pause 0.5
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
