init:
    $ goon_clothing_options = ['b_dressed']

init python:


    renpy.image('goon_arms_a_empty', 'ground.png')
    renpy.image('goon_body_b_empty', 'ground.png')
    renpy.image('goon_face_f_empty', 'ground.png')
    renpy.image('goon_face_talk_f_empty', 'ground.png')


    renpy.image('goon_face_talk_f_laugh', 'goon_face_f_laugh')



layeredimage goon:

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







    group face if_not 'm_talk' if_any goon_clothing_options auto











    group face if_all 'm_talk' if_any goon_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'goon_arms_dressed_a_sides'






    group overlay auto:
        attribute o_empty default null

image goon_f = "characters/goon/goon_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
