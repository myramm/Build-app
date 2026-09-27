init:
    $ lily_clothing_options = ['b_casual','b_naked','b_naked_pregnant_bump','b_naked_pregnant_belly','b_squeeze']

init python:


    renpy.image('lily_arms_a_empty', 'ground.png')
    renpy.image('lily_body_b_empty', 'ground.png')
    renpy.image('lily_face_f_empty', 'ground.png')
    renpy.image('lily_face_talk_f_empty', 'ground.png')


    renpy.image('lily_face_talk_f_laugh', 'lily_face_f_laugh')
    renpy.image('lily_face_talk_f_surprised', 'lily_face_f_surprised')
    renpy.image('lily_face_talk_f_wink', 'lily_face_f_wink')
    renpy.image('lily_face_talk_f_shy', 'lily_face_f_shy')



layeredimage lily:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_casual default
        attribute b_empty null


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any lily_clothing_options auto


    group face if_not 'm_talk' if_all 'b_hug' auto:
        offset (-76, 18)











    group face if_all 'm_talk' if_any lily_clothing_options auto variant 'talk'


    group face if_all ['m_talk','b_hug'] auto variant 'talk':
        offset (-76, 18)







    group arms if_all 'b_casual' auto variant 'casual':
        attribute a_idle default 'lily_arms_casual_a_sides'






    group overlay auto:
        attribute o_empty default null

image lily_f = "characters/lily/lily_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
