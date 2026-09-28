init:
    $ somrak_clothing_options = ['b_dressed']

init python:


    renpy.image('somrak_arms_dressed_a_empty', 'ground.png')
    renpy.image('somrak_body_b_empty', 'ground.png')
    renpy.image('somrak_face_f_empty', 'ground.png')
    renpy.image('somrak_face_talk_f_empty', 'ground.png')


    renpy.image('somrak_face_talk_f_laugh', 'somrak_face_f_laugh')
    renpy.image('somrak_face_talk_f_surprised', 'somrak_face_f_surprised')
    renpy.image('somrak_face_talk_f_angry', 'somrak_face_f_angry')
    renpy.image('somrak_face_talk_f_closed', 'somrak_face_f_closed')



layeredimage somrak:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any somrak_clothing_options auto











    group face if_all 'm_talk' if_any somrak_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'somrak_arms_dressed_a_cane'
        attribute a_hand_panties "somrak_arms_dressed_a_hand_panties"
        attribute a_smell "somrak_arms_dressed_a_smell"
        attribute a_lick "somrak_arms_dressed_a_lick"    






    group overlay auto:
        attribute o_empty default null

image somrak_f = "characters/somrak/somrak_face_f_normal.png"

image somrak_arms_dressed_a_hand_panties = ConditionSwitch(
    "M_somrak.get('delivered_panties') == 'Debbie'", "characters/somrak/somrak_arms_dressed_a_hand_panties_debbie.png",
    "M_somrak.get('delivered_panties') == 'Jenny'", "characters/somrak/somrak_arms_dressed_a_hand_panties_jenny.png",
    "M_somrak.get('delivered_panties') == 'Roxxy'", "characters/somrak/somrak_arms_dressed_a_hand_panties_roxxy.png",
    "M_somrak.get('delivered_panties') == 'Mia'", "characters/somrak/somrak_arms_dressed_a_hand_panties_mia.png",
    "M_somrak.get('delivered_panties') == 'Eve'", "characters/somrak/somrak_arms_dressed_a_hand_panties_eve.png",
    "M_somrak.get('delivered_panties') == 'Grace'", "characters/somrak/somrak_arms_dressed_a_hand_panties_grace.png",
    "M_somrak.get('delivered_panties') == 'Odette'", "characters/somrak/somrak_arms_dressed_a_hand_panties_odette.png",
    "M_somrak.get('delivered_panties') == 'Bridget'", "characters/somrak/somrak_arms_dressed_a_hand_panties_bridget.png",
    )

image somrak_arms_dressed_a_smell = ConditionSwitch(
    "M_somrak.get('delivered_panties') == 'Debbie'", "characters/somrak/somrak_arms_dressed_a_smell_debbie.png",
    "M_somrak.get('delivered_panties') == 'Jenny'", "characters/somrak/somrak_arms_dressed_a_smell_jenny.png",
    "M_somrak.get('delivered_panties') == 'Roxxy'", "characters/somrak/somrak_arms_dressed_a_smell_roxxy.png",
    "M_somrak.get('delivered_panties') == 'Mia'", "characters/somrak/somrak_arms_dressed_a_smell_mia.png",
    "M_somrak.get('delivered_panties') == 'Eve'", "characters/somrak/somrak_arms_dressed_a_smell_eve.png",
    "M_somrak.get('delivered_panties') == 'Grace'", "characters/somrak/somrak_arms_dressed_a_smell_grace.png",
    "M_somrak.get('delivered_panties') == 'Odette'", "characters/somrak/somrak_arms_dressed_a_smell_odette.png",
    "M_somrak.get('delivered_panties') == 'Bridget'", "characters/somrak/somrak_arms_dressed_a_smell_bridget.png",
    )

image somrak_arms_dressed_a_lick:
    Transform("characters/somrak/somrak_arms_dressed_a_lick1.png")
    pause .4
    Transform("characters/somrak/somrak_arms_dressed_a_lick2.png")
    pause .4
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
