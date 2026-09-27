init:
    $ bankguard_clothing_options = ['b_dressed', 'b_naked']

init python:


    renpy.image('bankguard_arms_a_empty', 'ground.png')
    renpy.image('bankguard_body_b_empty', 'ground.png')
    renpy.image('bankguard_face_f_empty', 'ground.png')
    renpy.image('bankguard_face_talk_f_empty', 'ground.png')


    renpy.image('bankguard_face_talk_f_laugh', 'bankguard_face_f_laugh')
    renpy.image('bankguard_face_talk_f_yawn', 'bankguard_face_f_yawn')



layeredimage bankguard:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed_sleep default
        attribute b_empty null


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null



































    group overlay auto:
        attribute o_empty default null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
