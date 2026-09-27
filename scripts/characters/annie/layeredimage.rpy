init:
    $ annie_clothing_options = ['b_dressed','b_naked']

init python:


    renpy.image('annie_arms_a_empty', 'ground.png')
    renpy.image('annie_body_b_empty', 'ground.png')
    renpy.image('annie_face_f_empty', 'ground.png')
    renpy.image('annie_face_talk_f_empty', 'ground.png')


    renpy.image('annie_face_talk_f_laugh', 'annie_face_f_laugh')
    renpy.image('annie_face_talk_f_eyeroll', 'annie_face_f_eyeroll')



layeredimage annie:

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







    group face if_not 'm_talk' if_any annie_clothing_options auto











    group face if_all 'm_talk' if_any annie_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'annie_arms_dressed_a_back'


    group arms if_all 'b_naked' auto variant 'naked':
        attribute a_idle default 'annie_arms_naked_a_sides'


    group overlay auto:
        attribute o_empty default null

image a = "characters/annie/layeredimage/annie_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
