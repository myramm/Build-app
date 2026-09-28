label eveX1_lewd:
    scene location_tattoo_bedroom_bed_side
    show eve b_pajamas_sleeping01 f_calm_close
    show anon a_empty b_empty f_normal_back_low:
        offset (-266.5, 45.5) subpixel True xzoom -.78 yzoom .78
    pause
    hide anon
    show eve b_pajamas_sleeping02
    with dissolve
    pause
    show eve b_pajamas_sleeping03 with dissolve
    pause
    eve @ -m_talk "Mmm."
    eve "{b}[firstname]{/b}?"
    anon "Good morning, sleepyhead."
    eve f_happy_close "Heh!"

    scene location_tattoo_bedroom_bed_top
    show eve a_belly b_pajamas_bed_back f_yawn m_talk
    show anon a_down b_sleep_side_eve f_sleep_side_normal
    show eve_overlay_o_blanket as blanket
    with fade
    eve -m_talk "{i}*Yawn*{/i}"
    eve a_belly b_pajamas_bed_side f_happy "What time is it?"
    anon "I dunno, like ten o'clock?"
    eve f_concerned "Ugh, so early?"
    eve "Let's go back to sleep."
    anon f_sleep_side_sexy "What, do you plan to sleep the whole day away?"
    eve f_happy "Yes."
    show eve b_pajamas_bed_back f_calm with {'master': dissolve}
    eve "Especially now that you're here to snuggle me."
    anon f_sleep_side_normal "Oh, so that's gonna be your excuse, huh?"
    show anon a_hold b_sleep_side_eve_cuddle f_sleep_side_sexy
    show eve a_empty
    show eve_arms_pajamas_bed_back_a_belly as eve_arm_left behind blanket:
        crop (680, 0, 344, 768) xalign 1.
    show eve_arms_pajamas_bed_back_a_belly as eve_arm_right behind anon:
        crop (0, 0, 680, 768)
    with {'master': dissolve}
    eve f_laugh @ -m_talk "Hehe!"
    show anon f_sleep_side_normal_closed
    show eve f_calm
    pause
    anon "It does feel nice."
    eve "Right?"
    pause
    anon "You're so soft, {b}Eve{/b}."
    pause
    anon "And warm."
    eve @ -m_talk "Mhmm."
    pause
    anon "Man, you smell good too!"
    anon f_sleep_side_normal "Like fresh baked cookies."
    eve "Heh, less talking, more sleeping!"
    anon f_sleep_side_sexy "I can think of something more fun than sleep."
    eve "Nothing is more fun than sleep."
    anon "You sure about that?"
    eve "Yes."
    hide eve_arm_left
    hide eve_arm_right
    show anon b_sleep_side_eve_kiss
    eve a_down f_gasping "{i}*Gasp*{/i}"
    eve f_calm "Oh, that's no fair... "
    anon b_sleep_side_eve_cuddle f_sleep_side_normal "Mmm, you taste good too."
    show anon b_sleep_side_eve_kiss with dissolve
    eve "... Heh, you're fighting dirty."
    show eve f_lipbite
    pause
    eve @ -m_talk "Ngh!"
    pause
    show anon b_sleep_side_eve_cuddle
    show eve a_empty b_pajamas_bed_side f_sexy
    show eve_arms_pajamas_bed_side_a_belly as eve_arm_left behind blanket:
        crop (680, 0, 344, 768) xalign 1.
    show eve_arms_pajamas_bed_side_a_belly as eve_arm_right behind anon:
        crop (0, 0, 680, 768)
    with dissolve
    pause
    hide anon
    hide eve_arm_left
    hide eve_arm_right
    show eve b_pajamas_bed_side_kiss
    with dissolve
    eve @ -m_talk "Mmm."
    pause
    show anon a_touch b_sleep_side_eve f_sleep_side_sexy behind blanket
    show eve a_belly b_pajamas_bed_side f_happy
    with {'master': dissolve}
    eve "Cheater."
    anon "Still wanna go back to sleep?"
    eve "No."
    anon "Heh."
    hide anon
    show eve b_pajamas_bed_side_kiss
    with dissolve
    eve "Mmm."
    pause
    show anon a_touch b_sleep_side_eve f_sleep_side_normal behind blanket
    show eve a_belly b_pajamas_bed_side f_happy
    with dissolve
    eve "Help me get these pajama bottoms off."
    anon "With pleasure!"

    $ renpy.dynamic(gender='trans' if M_eve.get('biggus_dickus') else 'cis',
                    anal=not M_eve.get('sex_front_1st_time'))
    call scene_eve_sex_wake.repeat (gender, anal)
    $ unlock_scene('Eve', '07_unlocked', variant=gender)
    if gender == 'cis' and anal:
        $ unlock_scene('Eve', '07_unlocked', variant='cis anal')

    scene location_tattoo_bedroom_bed_side
    show eve b_pajamas_sleeping03 f_happy_close
    with fade
    eve @ -m_talk "Mmm."
    eve "I could get used to waking up like that..."
    anon "Yeah?"
    pause
    anon "Well, I could get used to falling asleep like this."
    eve "Me too."
    pause
    eve "I love you, {b}[firstname]{/b}."

    menu:
        "I love you too.":
            anon "I love you too."
            eve "You're the best thing that's ever happened to me."
            anon "Likewise, {b}Evie{/b}."
        "Sleep.":

            pause
            eve f_curious_back "Did you hear me, {b}[firstname]{/b}?"
            anon "Zzz..."
            show eve f_sad_down
            pause
            show eve f_calm_close

    pause

    scene expression background(440, 304, 3.2, o=1) as stage with longfade
    show anon a_rub b_shirt f_yawn with {'master': dissolve}:
        xoffset -250 xzoom -1
    anon @ -m_talk "{i}*Yawn*{/i}"
    show anon b_shirt_undress_bottom with dissolve
    pause
    show anon a_sides b_dressed f_happy_back_low with {'master': dissolve}
    anon "{b}Eve{/b}?"
    show anon f_confused_low with {'master': dissolve}:
        xoffset 250 xzoom 1
    pause
    anon a_thinking f_thinking_down @ -m_talk "( Hmm, she must have woken up before me... )"
    show anon a_sides f_confused with {'master': dissolve}:
        xoffset -250 xzoom -1
    anon @ -m_talk "( ... And it sounds like {b}the shower is running{/b}. )"
    pause
    anon f_grin @ -m_talk "( I wonder if she'd be interested in a little company? )"
    hide anon with dissolve
    return


label eveX1_lewd.fail:
    scene location_tattoo_bedroom_bed_side
    show eve b_pajamas_sleeping01 f_calm_close
    show anon a_empty b_empty f_happy_back_low:
        offset (-266.5, 45.5) subpixel True xzoom -.78 yzoom .78
    anon @ -m_talk "( Aww, she looks so peaceful and cute... )"
    anon @ -m_talk "( I don't wanna ruin it. )"
    pause
    anon f_normal_back_low @ -m_talk "( I'll just come back later in the day and speak with her then. )"
    anon f_happy_back_low @ -m_talk "( Sweet dreams, {b}Eve{/b}. )"

    scene black with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
