init:
    $ judith_clothing_options = ['b_dressed','b_shorts','b_jersey','b_naked','b_magic','b_dressed_remove01','b_dressed_remove04','b_dressed_remove05','b_naked_cover','b_pants','b_undies']

init python:


    renpy.image('judith_arms_a_empty', 'ground.png')
    renpy.image('judith_body_b_empty', 'ground.png')
    renpy.image('judith_face_f_empty', 'ground.png')
    renpy.image('judith_face_talk_f_empty', 'ground.png')


    renpy.image('judith_face_talk_f_laugh', 'judith_face_f_laugh')


    renpy.image('judith_face_f_yell', 'judith_face_talk_f_yell')

layeredimage judith:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_magic "judith_body_b_[M_judith.outfit.get][M_judith.pregnancy.to_string]"   



    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any judith_clothing_options auto











    group face if_all 'm_talk' if_any judith_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'judith_arms_dressed_a_front'


    group arms if_all 'b_jersey' auto variant 'jersey':
        attribute a_idle default 'judith_arms_jersey_a_front'


    group arms if_any ['b_naked','b_pants','b_undies','b_shorts'] auto variant 'naked':
        attribute a_idle default 'judith_arms_naked_a_front'






    group overlay auto:
        attribute o_empty default null

image judith_f = "characters/judith/layeredimage/judith_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
