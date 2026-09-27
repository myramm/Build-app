init:
    $ missy_clothing_options = ['b_dressed', 'b_naked', 'b_undies']

init python:


    renpy.image('missy_arms_a_empty', 'ground.png')
    renpy.image('missy_body_b_empty', 'ground.png')
    renpy.image('missy_face_f_empty', 'ground.png')
    renpy.image('missy_face_talk_f_empty', 'ground.png')


    renpy.image('missy_face_talk_f_laugh', 'missy_face_f_laugh')
    renpy.image('missy_face_talk_f_yawn', 'missy_face_f_yawn')



layeredimage missy:

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







    group face if_not 'm_talk' if_any missy_clothing_options auto











    group face if_all 'm_talk' if_any missy_clothing_options auto variant 'talk'







    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'missy_arms_dressed_a_sides'


    group arms if_any ['b_undies'] auto variant 'undies':
        attribute a_idle default 'missy_arms_undies_a_hips'






    group overlay auto:
        attribute o_empty default null

image missy_f = "characters/missy/layeredimage/missy_face_f_normal.png"





image xray_missy_3some_beach:
    Transform("characters/xray/xray_top_01.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_02.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_03.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_04.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_05.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_06.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_07.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_08.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_09.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_10.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_11.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_12.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_13.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_14.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_15.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_16.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_17.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 0.4
    Transform("characters/xray/xray_top_18.png", zoom=.6, rotate=50, xoffset=300, yoffset=290)
    pause 2.0
    linear 2.5 alpha 0

image x = "characters/xray/xray_side_01.png"

image xray_missy_1o1_beach:
    Transform("characters/xray/xray_side_01.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-.7, yzoom=.7, xoffset=435, yoffset=250)
    pause 2.0
    linear 2.5 alpha 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
