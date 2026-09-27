init:
    $ earl_clothing_options = ['b_dressed', 'b_dressed_hug_harrold']

init python:


    renpy.image('earl_arms_a_empty', 'ground.png')
    renpy.image('earl_body_b_empty', 'ground.png')
    renpy.image('earl_face_f_empty', 'ground.png')
    renpy.image('earl_face_talk_f_empty', 'ground.png')


    renpy.image('earl_face_talk_f_laugh', 'earl_face_f_laugh')
    renpy.image('earl_face_talk_f_eat', 'earl_face_f_eat')



layeredimage earl:

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







    group face if_not 'm_talk' if_any earl_clothing_options auto











    group face if_all 'm_talk' if_any earl_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'earl_arms_dressed_a_donut'






    group overlay auto:
        attribute o_empty default null

image earl_f = "characters/earl/earl_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
