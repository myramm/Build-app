init:
    $ thug_clothing_options = ['b_dressed','b_dressed_leaning']

init python:


    renpy.image('thug_arms_a_empty', 'ground.png')
    renpy.image('thug_body_b_empty', 'ground.png')
    renpy.image('thug_face_f_empty', 'ground.png')
    renpy.image('thug_face_talk_f_empty', 'ground.png')


    renpy.image('thug_face_talk_f_laugh', 'thug_face_f_laugh')




    renpy.image('thug_arms_dressed_a_gun', 'goon_arms_dressed_a_gun')
    renpy.image('thug_arms_dressed_a_money_count', 'goon_arms_dressed_a_money_count')
    renpy.image('thug_arms_dressed_a_point', 'goon_arms_dressed_a_point')
    renpy.image('thug_arms_dressed_a_sides', 'goon_arms_dressed_a_sides')
    renpy.image('thug_arms_dressed_a_thinking', 'goon_arms_dressed_a_thinking')


layeredimage thug:

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







    group face if_not 'm_talk' if_any thug_clothing_options auto

    group face if_not 'm_talk' if_any 'b_dressed_bend' auto:
        offset (-52, 254)











    group face if_all 'm_talk' if_any thug_clothing_options auto variant 'talk'

    group face if_all 'm_talk' if_any 'b_dressed_bend' auto variant 'talk':
        offset (-52, 254)







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'thug_arms_dressed_a_sides'
        attribute a_boobs
        attribute a_cheer


    group arms if_all 'b_dressed_leaning' auto variant 'dressed_leaning':
        attribute a_idle default 'thug_arms_dressed_leaning_a_bottle'






    group overlay auto:
        attribute o_empty default null

image thug_f = "characters/thug/thug_face_f_normal.png"

image thug_arms_dressed_a_boobs:
    'thug_arms_dressed_a_boobs1'
    .4
    'thug_arms_dressed_a_boobs2'
    .4
    repeat


image thug_arms_dressed_a_cheer:
    'thug_arms_dressed_a_cheer1'
    'thug_arms_dressed_a_cheer2' with dissolve
    .5
    'thug_arms_dressed_a_cheer1' with dissolve
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
