init:
    $ ronda_clothing_options = ['b_dressed','b_naked','b_swim','b_jersey','b_underwear']
    $ ronda_chair_options = ['b_chair1','b_chair2','b_chair3']

init python:


    renpy.image('ronda_arms_a_empty', 'ground.png')
    renpy.image('ronda_body_b_empty', 'ground.png')
    renpy.image('ronda_face_f_empty', 'ground.png')
    renpy.image('ronda_face_talk_f_empty', 'ground.png')


    renpy.image('ronda_face_talk_f_laugh', 'ronda_face_f_laugh')


    renpy.image('ronda_face_f_surprised_down', 'ronda_face_talk_f_surprised_down')

layeredimage ronda:

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







    group face if_not 'm_talk' if_any ronda_clothing_options auto


    group face if_not 'm_talk' if_any ronda_chair_options auto:
        offset (-18,54)
        xzoom -1











    group face if_all 'm_talk' if_any ronda_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ronda_chair_options auto variant 'talk':
        offset (-18,54)
        xzoom -1







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'ronda_arms_dressed_a_sides'


    group arms if_all 'b_jersey' auto variant 'jersey':
        attribute a_idle default 'ronda_arms_jersey_a_sides'


    group arms if_all 'b_swim' auto variant 'swim':
        attribute a_idle default 'ronda_arms_swim_a_sides'


    group arms if_any ['b_naked'] auto variant 'naked':
        attribute a_idle default 'ronda_arms_naked_a_sides'


    group overlay auto:
        attribute o_empty default null

image ronda_f = "characters/ronda/ronda_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
