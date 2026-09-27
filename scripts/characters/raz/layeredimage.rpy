init:
    $ raz_clothing_options = ['b_dressed']

init python:


    renpy.image('raz_arms_a_empty', 'ground.png')
    renpy.image('raz_body_b_empty', 'ground.png')
    renpy.image('raz_face_f_empty', 'ground.png')
    renpy.image('raz_face_talk_f_empty', 'ground.png')


    renpy.image('raz_face_talk_f_laugh', 'raz_face_f_laugh')
    renpy.image('raz_face_talk_f_surprised_down', 'raz_face_f_surprised_down')


    renpy.image('raz_cutscene35_face_f_surprised', 'raz_cutscene35_face_talk_f_surprised')

layeredimage raz:

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







    group face if_not 'm_talk' if_any raz_clothing_options auto











    group face if_all 'm_talk' if_any raz_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'raz_arms_dressed_a_sides'






    group overlay auto:
        attribute o_empty default null


layeredimage raz cutscene33:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default null
    group face if_all 'm_talk' auto variant 'talk'


layeredimage raz cutscene35:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk'


layeredimage raz cutscene41:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default null
    group face if_all 'm_talk' auto variant 'talk'


layeredimage raz cutscene42:
    group mouth prefix 'm':
        attribute talk null

    group face if_not 'm_talk' auto:
        attribute f_normal default null
    group face if_all 'm_talk' auto variant 'talk'


image raz_f = "characters/raz/raz_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
