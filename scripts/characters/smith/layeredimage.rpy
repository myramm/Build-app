init:
    $ smith_clothing_options = ['b_dressed','b_naked']

init python:


    renpy.image('smith_arms_a_empty', 'ground.png')
    renpy.image('smith_body_b_empty', 'ground.png')
    renpy.image('smith_face_f_empty', 'ground.png')
    renpy.image('smith_face_talk_f_empty', 'ground.png')


    renpy.image('smith_face_talk_f_laugh', 'smith_face_f_laugh')
    renpy.image('smith_face_talk_f_scream', 'smith_face_f_scream')
    renpy.image('smith_face_talk_f_puke', 'smith_face_f_puke')



layeredimage smith:

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







    group face if_not 'm_talk' if_any smith_clothing_options auto











    group face if_all 'm_talk' if_any smith_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'smith_arms_dressed_a_ruler'






    group overlay auto:
        attribute o_empty default null

image smith_f = "characters/smith/smith_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
