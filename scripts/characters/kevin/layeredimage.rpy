init:
    $ kevin_clothing_options = ['b_dressed','b_apron']

init python:


    renpy.image('kevin_arms_a_empty', 'ground.png')
    renpy.image('kevin_body_b_empty', 'ground.png')
    renpy.image('kevin_face_f_empty', 'ground.png')
    renpy.image('kevin_face_talk_f_empty', 'ground.png')


    renpy.image('kevin_face_talk_f_laugh', 'kevin_face_f_laugh')


    renpy.image('kevin_face_f_bro', 'kevin_face_talk_f_bro')

layeredimage kevin:

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







    group face if_not 'm_talk' if_any kevin_clothing_options auto











    group face if_all 'm_talk' if_any kevin_clothing_options auto variant 'talk'







    group arms if_any ['b_dressed', 'b_apron'] auto variant 'dressed':
        attribute a_idle default 'kevin_arms_dressed_a_sides'






    group overlay auto:
        attribute o_empty default null

image k = "characters/kevin/layeredimage/kevin_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
