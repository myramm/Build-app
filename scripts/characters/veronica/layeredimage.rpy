init:
    $ vero_clothing_options = ['b_dressed','b_naked','b_disheveled','b_casual','b_empty']

init python:


    renpy.image('vero_arms_a_empty', 'ground.png')
    renpy.image('vero_body_b_empty', 'ground.png')
    renpy.image('vero_face_f_empty', 'ground.png')
    renpy.image('vero_face_talk_f_empty', 'ground.png')


    renpy.image('vero_face_talk_f_laugh', 'vero_face_f_laugh')
    renpy.image('vero_face_talk_f_surprised', 'vero_face_f_surprised')
    renpy.image('vero_face_talk_f_eyeroll', 'vero_face_f_eyeroll')
    renpy.image('vero_face_talk_f_thinking', 'vero_face_f_thinking')
    renpy.image('vero_face_talk_f_surprised_down', 'vero_face_f_surprised_down')



layeredimage vero:

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







    group face if_not 'm_talk' if_any vero_clothing_options auto











    group face if_all 'm_talk' if_any vero_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'vero_arms_dressed_a_front'


    group arms if_any ['b_disheveled'] auto variant 'disheveled':
        attribute a_idle default 'vero_arms_disheveled_a_hip'


    group arms if_any ['b_casual'] auto variant 'casual':
        attribute a_idle default 'vero_arms_casual_a_front'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'vero_arms_naked_a_front'


    group overlay auto:
        attribute o_empty default null

image vero_f = "characters/vero/vero_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
