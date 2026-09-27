init:
    $ kim_clothing_options = ['b_dressed']

init python:


    renpy.image('kim_arms_a_empty', 'ground.png')
    renpy.image('kim_body_b_empty', 'ground.png')
    renpy.image('kim_face_f_empty', 'ground.png')
    renpy.image('kim_face_talk_f_empty', 'ground.png')


    renpy.image('kim_face_talk_f_laugh', 'kim_face_f_laugh')
    renpy.image('kim_face_talk_f_surprised', 'kim_face_f_surprised')
    renpy.image('kim_face_talk_f_surprised_down', 'kim_face_f_surprised_down')



layeredimage kim:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_dressed_reach 'kim_body_b_dressed_reach'


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any kim_clothing_options auto


    group face if_not 'm_talk' if_any ['b_dressed_reach','b_dressed_reach1'] auto:
        offset (-122,65)











    group face if_all 'm_talk' if_any kim_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_dressed_reach','b_dressed_reach1'] auto variant 'talk':
        offset (-122,65)







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'kim_arms_dressed_a_counter'
        attribute a_empty null






    group overlay auto:
        attribute o_empty default null

image kim_f = "characters/kim/kim_face_f_normal.png"

image kim_body_b_dressed_reach:
    Transform("kim_body_b_dressed_reach1")
    pause .2
    Transform("kim_body_b_dressed_reach2")
    pause .2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
