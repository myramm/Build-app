init:
    $ harold_clothing_options = ['b_dressed', 'b_tanktop', 'b_tanktop_bandage', 'b_tanktop_hug', 'b_disheveled', 'b_empty']

init python:


    renpy.image('harold_arms_a_empty', 'ground.png')
    renpy.image('harold_body_b_empty', 'ground.png')
    renpy.image('harold_face_f_empty', 'ground.png')
    renpy.image('harold_face_talk_f_empty', 'ground.png')


    renpy.image('harold_face_talk_f_laugh', 'harold_face_f_laugh')



layeredimage harold:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_tanktop_bandage 'harold_body_b_tanktop'


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any harold_clothing_options auto


    group face if_not 'm_talk' if_any ['b_tanktop_injured'] auto:
        offset (-99, 138)


    group face if_not 'm_talk' if_any ['b_dressed_floor'] auto:
        offset (-366,-110)











    group face if_all 'm_talk' if_any harold_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_tanktop_injured'] auto variant 'talk':
        offset (-99, 138)


    group face if_all 'm_talk' if_any ['b_dressed_floor'] auto variant 'talk':
        offset (-366,-110)







    group arms if_any ['b_dressed', 'b_disheveled'] auto variant 'dressed':
        attribute a_idle default 'harold_arms_dressed_a_sides'


    group arms if_any ['b_tanktop'] auto variant 'tanktop':
        attribute a_idle default 'harold_arms_tanktop_a_sides'


    group arms if_any ['b_tanktop_bandage'] auto variant 'tanktop_bandage':
        attribute a_idle default 'harold_arms_tanktop_bandage_a_sides'


    group arms if_any ['b_dressed_floor'] auto variant 'dressed_floor':
        attribute a_idle default 'harold_arms_dressed_floor_a_yumi'






    group overlay auto:
        attribute o_empty default null

image harold_f = "characters/harold/layeredimage/harold_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
