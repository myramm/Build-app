init:
    $ yumi_clothing_options = ['b_dressed', 'b_disheveled', 'b_dressed_hug_debbie', 'b_empty']

init python:


    renpy.image('yumi_arms_a_empty', 'ground.png')
    renpy.image('yumi_body_b_empty', 'ground.png')
    renpy.image('yumi_face_f_empty', 'ground.png')
    renpy.image('yumi_face_talk_f_empty', 'ground.png')


    renpy.image('yumi_face_talk_f_laugh', 'yumi_face_f_laugh')
    renpy.image('yumi_face_car_talk_f_laugh', 'yumi_face_car_f_laugh')



layeredimage yumi:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_searching_mc Transform("characters/yumi/layeredimage/yumi_body_b_searching_mc.png",xzoom=-1,xoffset=-473)
        attribute b_searching_eve Image("characters/yumi/layeredimage/yumi_body_b_searching_eve.png",xoffset=-360)


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any yumi_clothing_options auto


    group face if_not 'm_talk' if_any ['b_dressed_hurt_floor'] auto:
        xzoom -1
        rotate -16
        offset (-232,-288)






    group face if_not 'm_talk' if_any ['b_dressed_car_front'] auto variant 'car'







    group face if_all 'm_talk' if_any yumi_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_dressed_hurt_floor'] auto variant 'talk':
        xzoom -1
        rotate -16
        offset (-232,-288)






    group face if_all 'm_talk' if_any ['b_dressed_car_front'] auto variant 'car_talk'



    group arms if_any ['b_dressed', 'b_disheveled'] auto variant 'dressed':
        attribute a_idle default 'yumi_arms_dressed_a_sides'


    group arms if_any ['b_dressed_car_front'] auto variant 'dressed_car':
        attribute a_idle default 'yumi_arms_dressed_car_a_down'


    group arms if_any ['b_dressed_hurt_floor'] auto variant 'dressed_hurt_floor':
        attribute a_idle default 'yumi_arms_dressed_hurt_floor_a_wound'






    group overlay if_not ['b_dressed_hurt_floor'] auto:
        attribute o_empty default null

    group overlay if_any ['b_dressed_hurt_floor'] auto:
        xzoom -1
        rotate -16
        offset (-232, -288)

image yumi_f = "characters/yumi/layeredimage/yumi_face_f_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
