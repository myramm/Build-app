init:
    $ lucy_clothing_options = ['b_dressed','b_messy']

init python:


    renpy.image('lucy_arms_a_empty', 'ground.png')
    renpy.image('lucy_body_b_empty', 'ground.png')
    renpy.image('lucy_face_f_empty', 'ground.png')
    renpy.image('lucy_face_talk_f_empty', 'ground.png')


    renpy.image('lucy_face_talk_f_laugh', 'lucy_face_f_laugh')
    renpy.image('lucy_face_talk_f_surprised', 'lucy_face_f_surprised')
    renpy.image('lucy_face_talk_f_yell', 'lucy_face_f_yell')
    renpy.image('lucy_face_talk_f_thinking', 'lucy_face_f_thinking')
    renpy.image('lucy_face_talk_f_eyeroll', 'lucy_face_f_eyeroll')
    renpy.image('lucy_face_talk_f_bigsmile', 'lucy_face_f_bigsmile')



layeredimage lucy:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_hug_mc Image("characters/lucy/lucy_body_b_hug_mc.png",xoffset=-474)
        attribute b_kiss_mc Image("characters/lucy/lucy_body_b_kiss_mc.png",xoffset=-335)


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any lucy_clothing_options auto











    group face if_all 'm_talk' if_any lucy_clothing_options auto variant 'talk'







    group arms if_any ['b_dressed','b_messy'] auto variant 'dressed':
        attribute a_idle default 'lucy_arms_dressed_a_sides'






    group overlay auto:
        attribute o_empty default null

image lucy_f = "characters/lucy/lucy_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
