init:
    $ priya_clothing_options = ['b_dressed','b_naked']

init python:


    renpy.image('priya_arms_a_empty', 'ground.png')
    renpy.image('priya_body_b_empty', 'ground.png')
    renpy.image('priya_face_f_empty', 'ground.png')
    renpy.image('priya_face_talk_f_empty', 'ground.png')


    renpy.image('priya_face_talk_f_laugh', 'priya_face_f_laugh')
    renpy.image('priya_face_talk_f_surprised', 'priya_face_f_surprised')
    renpy.image('priya_face_talk_f_eyeroll', 'priya_face_f_eyeroll')



layeredimage priya:

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







    group face if_not 'm_talk' if_any priya_clothing_options auto











    group face if_all 'm_talk' if_any priya_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'priya_arms_dressed_a_sides'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'priya_arms_naked_a_sides'


    group overlay auto:
        attribute o_empty default null

image priya_f = "characters/priya/priya_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
