label scene_liu_sex_office:

    return


label scene_liu_sex_office.stage:
    scene location_bank_office_printer_sex
    show liu b_sex_printer_base
    return


label scene_liu_sex_office.pre:
    show liu b_sex_printer_insert
    return


label scene_liu_sex_office.insert:
    hide liu
    show liu_sex_printer_anim 5 as animation
    return


label scene_liu_sex_office.animate:
    python:
        anim_toggle = True
        animated = True
    hide anon
    hide liu
    show liu_sex_printer_anim as animation
    return


label scene_liu_sex_office.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show liu_sex_printer_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_liu_sex_office.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'liu_sex_printer_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_liu_sex_office.dialogue
        $ animcounter += 1
    call screen scene_liu_sex_office_controls
    if not _return:
        jump scene_liu_sex_office.loop
    return _return


label scene_liu_sex_office.dialogue:
    if animcounter == 0 and randomizer() > 75:
        liu "NGH!!{w=1}{nw}"
    elif animcounter == 0 and randomizer() > 75:
        liu "Ahh, fuck!!{w=1}{nw}"
        anon "Shh!{w=1}{nw}"
        anon "Someone will hear.{w=1}{nw}"
        pause 1
        liu "I can't-{w=1}{nw}"
        pause 1
        liu "Help it!{w=1}{nw}"
    elif animcounter == 1 and randomizer() > 75:
        liu "OH, GOD!{w=1}{nw}"
        liu "{b}[firstname!u]{/b}!!!{w=1}{nw}"
    elif animcounter == 2 and randomizer() > 75:
        anon "Gah, you're so tight!{w=1}{nw}"
        liu "{i}*Whimpers*{/i}{w=1}{nw}"
    return


label scene_liu_sex_office.switch:
    call scene_liu_sex_office.stage
    call scene_liu_sex_office.animate
    with fade
    jump scene_liu_sex_office.resume


label scene_liu_sex_office.cum(where):
    anon "I'm gonna cum!"
    liu "Hurry!"
    pause
    liu "Oh, god!!"
    liu "Oh my god!!"
    pause
    liu "{i}*Whimpers*{/i}"
    liu "NGGHHH!!!"
    hide animation
    if where == 'inside':
        show liu b_sex_printer_cum
    else:
        show liu b_sex_printer_base f_surprised_down od_cumshot
    anon "HNNGGG!!!" with flash
    if where == 'inside':
        show xray_liu_sex_printer with fastdissolve
        pause
        hide xray_liu_sex_printer with {'master': dissolve}
    else:
        show liu od_cumshot3
    anon "Haah... Haah..."
    return where


label scene_liu_sex_office.repeat:
    python hide:
        M_liu.set('sex speed', 1 / 8.)

    call scene_liu_sex_office.stage
    with fade
    liu "Like this?"
    anon "Just like that."
    liu "O-okay but go slow..."
    call scene_liu_sex_office.pre
    with dissolve
    liu "... We can't have the customers hearing-"
    call scene_liu_sex_office.insert
    liu "OOOHHH!!" with hpunch
    liu "USSS!"
    anon "Oh, wow!"
    call scene_liu_sex_office.animate
    with dissolve
    pause
    liu "NGH!!"
    pause
    liu "Ahh, fuck!!"
    anon "Shh!"
    pause
    anon "Someone will hear."
    liu "I can't-"
    liu "Help it!"
    pause
    liu "OH, GOD!"
    liu "{b}[firstname!u]{/b}!!!"
    pause
    anon "Gah, you're so tight!"
    liu "{i}*Whimpers*{/i}"
    pause
    label scene_liu_sex_office.resume:
    call scene_liu_sex_office.loop
    if _return == 'switch':
        jump scene_liu_sex_office_pov.switch
    call scene_liu_sex_office.cum (_return)
    $ renpy.dynamic(where=_return)

    if where == 'inside':
        show liu b_sex_printer_base o_dick_after with dissolve
        liu "I can't believe how hot that was..."
        anon "Y-yeah."
        liu "I came so hard... Oh my goodness!"
        pause
        liu @ -m_talk "Mmm."
        liu "How am I supposed to go back to work after that?!"
        anon "Hehe!"
        call call_pregnancy_minigame (None, M_liu)
    else:

        liu f_shy "Oh, wow..."
        liu "Heh, you came all over my suit!"
        anon "Ah man, I'm so sorry..."
        anon "... I didn't mean-"
        pause
        anon "It all happened so fast!"
        liu "No, it's okay."
        liu "It'll wash out..."
        liu "... I think."
        pause
        liu "I just hope {b}Tina{/b} doesn't see the stains this afternoon."

    return where


label scene_liu_sex_office.replay:
    jump scene_liu_sex_office.repeat


screen scene_liu_sex_office_controls(angle='side'):
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            if angle == 'side':
                textbutton _('Cum Inside') action Return('inside')
                textbutton _('Cum Outside') action Return('outside')
            textbutton _('Change angle') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_liu.set, 'sex speed',
                                 1 / (1 / M_liu.get('sex speed') - 2)),
                        Return(False))
                sensitive M_liu.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_liu.set, 'sex speed',
                                 1 / (1 / M_liu.get('sex speed') + 2)),
                        Return(False))
                sensitive M_liu.get('sex speed') > 1 / 12.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
