init:
    $ keeves_clothing_options = ['b_dressed','b_suit']

init python:


    renpy.image('keeves_arms_a_empty', 'ground.png')
    renpy.image('keeves_body_b_empty', 'ground.png')
    renpy.image('keeves_face_f_empty', 'ground.png')
    renpy.image('keeves_face_talk_f_empty', 'ground.png')


    renpy.image('keeves_face_talk_f_laugh', 'keeves_face_f_laugh')
    renpy.image('keeves_face_talk_f_eat', 'keeves_face_f_eat')
    renpy.image('keeves_face_talk_f_sing', 'keeves_face_f_sing')
    renpy.image('keeves_face_talk_f_ninja', 'keeves_face_f_ninja')



layeredimage keeves:

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







    group face if_not 'm_talk' if_any keeves_clothing_options auto











    group face if_all 'm_talk' if_any keeves_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'keeves_arms_dressed_a_sides'


    group arms if_all 'b_suit' auto variant 'suit':
        attribute a_idle default 'keeves_arms_suit_a_sides'
        attribute a_empty null






    group overlay auto:
        attribute o_empty default null

image keeves_f = "characters/keeves/keeves_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
