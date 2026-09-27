init:
    $ rump_clothing_options = ['b_dressed','b_jumpsuit']

init python:


    renpy.image('rump_arms_a_empty', 'ground.png')
    renpy.image('rump_body_b_empty', 'ground.png')
    renpy.image('rump_face_f_empty', 'ground.png')
    renpy.image('rump_face_talk_f_empty', 'ground.png')


    renpy.image('rump_face_talk_f_laugh', 'rump_face_f_laugh')
    renpy.image('rump_face_talk_f_eyeroll', 'rump_face_f_eyeroll')


    renpy.image('rump_face_f_lips', 'rump_face_talk_f_lips')

layeredimage rump:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_dressed_bending_robot "pantat_tubuh_b_berpakaian_bending_robot"



    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any rump_clothing_options auto


    group face if_not 'm_talk' if_any ["b_dressed_bending_robot","b_dressed_bending"] auto:
        offset (-95, 175)


    group face if_not 'm_talk' if_any ["b_jacuzzi"] auto:
        offset (-42, 102)











    group face if_all 'm_talk' if_any rump_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ["b_dressed_bending_robot","b_dressed_bending"] auto variant 'talk':
        offset (-95, 175)


    group face if_all 'm_talk' if_any ["b_jacuzzi"] auto variant 'talk':
        offset (-42, 102)







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'rump_arms_dressed_a_sides'
        attribute a_grope_robot 'rump_arms_dressed_a_grope_robot'


    group arms if_all 'b_jumpsuit' auto variant 'jumpsuit':
        attribute a_idle default 'rump_arms_jumpsuit_a_crossed'


    group arms if_all 'b_jacuzzi' auto variant 'jacuzzi':
        attribute a_idle default 'rump_arms_jacuzzi_a_phone'






    group overlay_jumpsuit auto:
        attribute o_empty default null

    group overlay auto:
        attribute o_empty default null

image rump_f = "characters/rump/rump_face_f_normal.png"

image rump_arms_dressed_a_grope_robot:
    Transform("rump_arms_dressed_a_grope_robot1")
    pause .4
    Transform("rump_arms_dressed_a_grope_robot2")
    pause .4
    repeat

image rump_body_b_dressed_bending_robot:
    Transform("rump_body_b_dressed_bending_robot1")
    pause .4
    Transform("rump_body_b_dressed_bending_robot2")
    pause .4
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
