init:
    $ frank_clothing_options = ['b_dressed','b_empty']

init python:


    renpy.image('frank_arms_a_empty', 'ground.png')
    renpy.image('frank_body_b_empty', 'ground.png')
    renpy.image('frank_face_f_empty', 'ground.png')
    renpy.image('frank_face_talk_f_empty', 'ground.png')


    renpy.image('frank_face_talk_f_laugh', 'frank_face_f_laugh')



layeredimage frank:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:

        attribute b_empty default null


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any frank_clothing_options auto











    group face if_all 'm_talk' if_any frank_clothing_options auto variant 'talk'











    group overlay auto:
        attribute o_empty default null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
