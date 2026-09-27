init:
    $ tony_clothing_options = ['b_dressed','b_casual_hug1','b_casual_hug2','b_casual_hug3','b_casual_bandage','b_dressed_pic','b_naked_shirt','b_naked','b_casual','b_dressed_hug','b_dressed_hug_mc','b_casual_hug_mc','b_empty']

init python:


    renpy.image('tony_arms_a_empty', 'ground.png')
    renpy.image('tony_body_b_empty', 'ground.png')
    renpy.image('tony_face_f_empty', 'ground.png')
    renpy.image('tony_face_talk_f_empty', 'ground.png')


    renpy.image('tony_face_talk_f_laugh', 'tony_face_f_laugh')


    renpy.image('tony_face_f_smirk_wink', 'tony_face_talk_f_smirk_wink')


    renpy.image('tony_arms_dressed_a_point', 'tony_arms_casual_a_point')
    renpy.image('tony_arms_dressed_a_wave', 'tony_arms_casual_a_wave')
    renpy.image('tony_arms_dressed_a_phone', 'tony_arms_casual_a_phone')
    renpy.image('tony_arms_dressed_a_phone_talk', 'tony_arms_casual_a_phone_talk')


layeredimage tony:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default
        attribute b_empty null
        attribute b_mcpuffin null
        attribute b_casual_bandage 'tony_body_b_casual'
        attribute b_casual_hug1 'tony_body_b_casual_hug1[M_maria.pregnancy]'
        attribute b_casual_hug2 'tony_body_b_casual_hug2[M_maria.pregnancy]'
        attribute b_casual_hug3 'tony_body_b_casual_hug3[M_maria.pregnancy]'


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any tony_clothing_options auto


    group face if_not 'm_talk' if_any ['b_casual_injured'] auto:
        offset (-61, 158)


    group face if_not 'm_talk' if_any 'b_casual_crane' auto:
        xoffset -79


    group face if_not 'm_talk' if_any 'b_dressed_slumped' auto:
        offset(-35, 20)






    group face if_not 'm_talk' if_any 'b_mcpuffin' auto variant 'briefcase':
        attribute f_normal default null







    group face if_all 'm_talk' if_any tony_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_casual_injured'] auto variant 'talk':
        offset (-61, 158)


    group face if_all 'm_talk' if_any 'b_casual_crane' auto variant 'talk':
        xoffset -79


    group face if_all 'm_talk' if_any 'b_dressed_slumped' auto variant 'talk':
        offset(-35, 20)






    group face if_all 'm_talk' if_any 'b_mcpuffin' auto variant 'briefcase_talk':
        attribute f_normal default 'tony_face_briefcase_talk_f_normal_down'



    group arms if_all 'b_dressed' auto variant 'dressed':
        attribute a_idle default 'tony_arms_dressed_a_hips'
        attribute a_empty null
        attribute a_scrub 'tony_arms_dressed_a_scrub'
        attribute a_baby 'tony_arms_dressed_a_baby_[M_maria.pregnancy.baby_gender]'
        attribute a_baby_phone 'tony_arms_dressed_a_baby_[M_maria.pregnancy.baby_gender]_phone'
        attribute a_tina_shoulder 'tony_arms_dressed_a_tina_shoulder[M_tina.pregnancy.to_string]'


    group arms if_any ['b_naked_shirt'] auto variant 'naked_shirt':
        attribute a_idle default 'tony_arms_naked_shirt_a_dick_side'
        attribute a_empty null
        attribute a_frustrated 'tony_arms_dressed_a_frustrated'
        attribute a_hips 'tony_arms_dressed_a_hips'
        attribute a_scrub 'tony_arms_dressed_a_scrub'


    group arms if_any ['b_casual'] auto variant 'casual':
        attribute a_idle default 'tony_arms_casual_a_hips'
        attribute a_empty null
        attribute a_scrub 'tony_arms_dressed_a_scrub'
        attribute a_energy_drink 'tony_arms_dressed_a_energy_drink'
        attribute a_finger_up 'tony_arms_dressed_a_finger_up'
        attribute a_fists 'tony_arms_dressed_a_fists'
        attribute a_frustrated 'tony_arms_dressed_a_frustrated'
        attribute a_point_back 'tony_arms_dressed_a_point_back'
        attribute a_pizza 'tony_arms_dressed_a_pizza'
        attribute a_mc_hip_single 'tony_arms_dressed_a_mc_hip_single'
        attribute a_pipe_hold_shoulder 'tony_arms_dressed_a_pipe_hold_shoulder'
        attribute a_pipe_hold 'tony_arms_dressed_a_pipe_hold'
        attribute a_arms_around 'tony_arms_dressed_a_arms_around'
        attribute a_point_under 'tony_arms_dressed_a_point_under'
        attribute a_mc_shoulder_single 'tony_arms_dressed_a_mc_shoulder_single'


    group arms if_any ['b_casual_bandage'] auto variant 'casual_bandage':
        attribute a_idle default 'tony_arms_casual_bandage_a_hips'


    group overlay auto:
        attribute o_empty default null

image tony_f = "characters/tony/tony_face_f_normal.png"

image tony_arms_dressed_a_scrub:
    Transform("tony_arms_dressed_a_scrub1")
    pause .4
    Transform("tony_arms_dressed_a_scrub2")
    pause .4
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
