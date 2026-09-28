init:
    $ tammy_clothing_options = ['b_yoga','b_empty','b_naked']

init python:


    renpy.image('tammy_arms_a_empty', 'ground.png')
    renpy.image('tammy_body_b_empty', 'ground.png')
    renpy.image('tammy_face_f_empty', 'ground.png')
    renpy.image('tammy_face_talk_f_empty', 'ground.png')


    renpy.image('tammy_face_talk_f_laugh', 'tammy_face_f_laugh')



layeredimage tammy:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_yoga default
        attribute b_empty null
        attribute b_magic "tammy_body_b_[M_tammy.outfit.get][M_tammy.pregnancy.to_string]"   


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any tammy_clothing_options auto















    group face if_all 'm_talk' if_any tammy_clothing_options auto variant 'talk'











    group arms if_all 'b_yoga' auto variant 'yoga':
        attribute a_idle default 'tammy_arms_yoga_a_hips'
        attribute a_watch 'tammy_arms_yoga_a_watch'











    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'tammy_arms_naked_a_hips'


    group overlay auto:
        attribute o_empty default null

image tammy_f = "characters/tammy/tammy_face_f_normal.png"

image tammy_arms_yoga_a_watch:
    "tammy_arms_yoga_a_watch1"
    pause .4
    "tammy_arms_yoga_a_watch2" with fastdissolve
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
