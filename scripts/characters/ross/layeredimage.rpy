init:
    $ ross_clothing_options = ['b_dressed','b_bottom','b_naked']

init python:


    renpy.image('ross_arms_a_empty', 'ground.png')
    renpy.image('ross_body_b_empty', 'ground.png')
    renpy.image('ross_face_f_empty', 'ground.png')
    renpy.image('ross_face_talk_f_empty', 'ground.png')


    renpy.image('ross_face_talk_f_laugh', 'ross_face_f_laugh')
    renpy.image('ross_face_talk_f_eyeroll', 'ross_face_f_eyeroll')



layeredimage ross:

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







    group face if_not 'm_talk' if_any ross_clothing_options auto











    group face if_all 'm_talk' if_any ross_clothing_options auto variant 'talk'







    group arms if_all'b_dressed' auto variant 'dressed':
        attribute a_idle default 'ross_arms_dressed_a_hip'


    group arms if_any ['b_naked', 'b_bottom'] auto variant 'naked':
        attribute a_idle default 'ross_arms_naked_a_hip'


    group overlay auto:
        attribute o_empty default null

image r = "characters/ross/layeredimage/ross_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
