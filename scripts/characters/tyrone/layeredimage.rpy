init:
    $ tyrone_clothing_options = ['b_dressed']

init python:


    renpy.image('tyrone_arms_a_empty', 'ground.png')
    renpy.image('tyrone_body_b_empty', 'ground.png')
    renpy.image('tyrone_face_f_empty', 'ground.png')
    renpy.image('tyrone_face_talk_f_empty', 'ground.png')


    renpy.image('tyrone_face_talk_f_laugh', 'tyrone_face_f_laugh')
    renpy.image('tyrone_face_talk_f_uneasy_down', 'tyrone_face_f_uneasy_down')



layeredimage tyrone:

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







    group face if_not 'm_talk' if_any tyrone_clothing_options auto











    group face if_all 'm_talk' if_any tyrone_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'tyrone_arms_dressed_a_sides'






    group overlay auto:
        attribute o_empty default null

image tyrone_f = "characters/tyrone/tyrone_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
