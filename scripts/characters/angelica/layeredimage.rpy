init:
    $ angelica_clothing_options = ['b_dressed']

init python:


    renpy.image('angelica_arms_a_empty', 'ground.png')
    renpy.image('angelica_body_b_empty', 'ground.png')
    renpy.image('angelica_face_f_empty', 'ground.png')
    renpy.image('angelica_face_talk_f_empty', 'ground.png')


    renpy.image('angelica_face_talk_f_laugh', 'angelica_face_f_laugh')
    renpy.image('angelica_face_talk_f_surprised_down', 'angelica_face_f_surprised_down')



layeredimage angelica:

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







    group face if_not 'm_talk' if_any angelica_clothing_options auto











    group face if_all 'm_talk' if_any angelica_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'angelica_arms_dressed_a_front'






    group overlay auto:
        attribute o_empty default null

image angelica_f = "characters/angelica/layeredimage/angelica_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
