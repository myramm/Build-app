init:
    $ olivia_clothing_options = ['b_swimsuit']

init python:


    renpy.image('olivia_arms_a_empty', 'ground.png')
    renpy.image('olivia_body_b_empty', 'ground.png')
    renpy.image('olivia_face_f_empty', 'ground.png')
    renpy.image('olivia_face_talk_f_empty', 'ground.png')


    renpy.image('olivia_face_talk_f_laugh', 'olivia_face_f_laugh')
    renpy.image('olivia_face_talk_f_surprised', 'olivia_face_f_surprised')



layeredimage olivia:

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







    group face if_not 'm_talk' if_any olivia_clothing_options auto











    group face if_all 'm_talk' if_any olivia_clothing_options auto variant 'talk'







    group arms if_all 'b_swimsuit' auto variant 'swimsuit':
        attribute a_idle default 'olivia_arms_swimsuit_a_sides'






    group overlay auto:
        attribute o_empty default null

image olivia_f = "characters/cassie/layeredimage/olivia_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
