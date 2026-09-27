init:
    $ anna_clothing_options = ['b_dressed','b_naked']

init python:


    renpy.image('anna_arms_a_empty', 'ground.png')
    renpy.image('anna_body_b_empty', 'ground.png')
    renpy.image('anna_face_f_empty', 'ground.png')
    renpy.image('anna_face_talk_f_empty', 'ground.png')


    renpy.image('anna_face_talk_f_laugh', 'anna_face_f_laugh')
    renpy.image('anna_face_talk_f_surprised', 'anna_face_f_surprised')



layeredimage anna:

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







    group face if_not 'm_talk' if_any anna_clothing_options auto











    group face if_all 'm_talk' if_any anna_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'anna_arms_dressed_a_hip'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'anna_arms_naked_a_hip'


    group overlay auto:
        attribute o_empty default null

image anna_f = "characters/anna/layeredimage/anna_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
