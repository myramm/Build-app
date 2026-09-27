init:
    $ richard_clothing_options = ['b_dressed']

init python:


    renpy.image('richard_arms_a_empty', 'ground.png')
    renpy.image('richard_body_b_empty', 'ground.png')
    renpy.image('richard_face_f_empty', 'ground.png')
    renpy.image('richard_face_talk_f_empty', 'ground.png')


    renpy.image('richard_face_talk_f_laugh', 'richard_face_f_laugh')
    renpy.image('richard_face_talk_f_surprised', 'richard_face_f_surprised')
    renpy.image('richard_face_talk_f_angry_yell', 'richard_face_f_angry_yell')
    renpy.image('richard_face_talk_f_stern_down', 'richard_face_f_stern_down')



layeredimage richard:

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







    group face if_not 'm_talk' if_any richard_clothing_options auto











    group face if_all 'm_talk' if_any richard_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'richard_arms_dressed_a_hips'






    group overlay auto:
        attribute o_empty default null

image richard_f = "characters/richard/richard_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
