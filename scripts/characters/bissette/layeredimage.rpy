init:
    $ bissette_clothing_options = ['b_dressed','b_naked']

init python:


    renpy.image('bissette_arms_a_empty', 'ground.png')
    renpy.image('bissette_body_b_empty', 'ground.png')
    renpy.image('bissette_face_f_empty', 'ground.png')
    renpy.image('bissette_face_talk_f_empty', 'ground.png')


    renpy.image('bissette_face_talk_f_laugh', 'bissette_face_f_laugh')


    renpy.image('bissette_face_f_yell', 'bissette_face_talk_f_yell')

layeredimage bissette:

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







    group face if_not 'm_talk' if_any bissette_clothing_options auto











    group face if_all 'm_talk' if_any bissette_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'bissette_arms_dressed_a_front'







    group overlay auto:
        attribute o_empty default null

image bissette_f = "characters/bissette/bissette_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
