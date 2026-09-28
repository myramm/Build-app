init:
    $ daisy_clothing_options = ['b_naked_boob','b_diane_milking','b_player_milking','b_naked','b_naked_flowers','b_naked_pregnant_bump','b_naked_pregnant_belly','b_naked_milking_shirtless2','b_naked_milking_shirtless1','b_naked_milking_naked2','b_naked_milking_naked1','b_naked_milking_cow2','b_naked_milking_cow1','b_naked_milking2_pregnant_bump','b_naked_milking1_pregnant_bump','b_naked_milking2_pregnant_belly','b_naked_milking1_pregnant_belly','b_naked_milking2','b_naked_milking1','b_naked_boob2_pregnant_bump','b_naked_boob1_pregnant_bump','b_naked_boob2_pregnant_belly','b_naked_boob1_pregnant_belly','b_naked_boob2','b_naked_boob1']

init python:


    renpy.image('daisy_arms_a_empty', 'ground.png')
    renpy.image('daisy_body_b_empty', 'ground.png')
    renpy.image('daisy_face_f_empty', 'ground.png')
    renpy.image('daisy_face_talk_f_empty', 'ground.png')


    renpy.image('daisy_face_talk_f_laugh', 'daisy_face_f_laugh')
    renpy.image('daisy_face_talk_f_eyeroll', 'daisy_face_f_eyeroll')
    renpy.image('daisy_face_talk_f_burp', 'daisy_face_f_burp')
    renpy.image('daisy_face_talk_f_surprised_after_appear', 'daisy_face_f_surprised_after_appear')
    renpy.image('daisy_face_talk_f_scared', 'daisy_face_f_scared')
    renpy.image('daisy_face_talk_f_surprised_low', 'daisy_face_f_surprised_low')



layeredimage daisy:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_naked default "characters/daisy/daisy_body_b_naked[M_daisy.pregnancy.to_string].png"
        attribute b_naked_flowers "characters/daisy/daisy_body_b_naked.png"
        attribute b_empty null
        attribute b_diane_milking "daisy_body_b_diane_milking"
        attribute b_player_milking "daisy_body_b_player_milking"
        attribute b_naked_behind_pickup "daisy_body_b_naked_behind_pickup"
        attribute b_naked_boob "daisy_body_b_naked_boob"
        attribute b_naked_cower "daisy_body_b_naked_cower[M_daisy.pregnancy.to_string]"
        attribute b_naked_blanket_cover1 "daisy_body_b_naked_blanket_cover1[M_daisy.pregnancy.to_string]"
        attribute b_naked_blanket_cover2 "daisy_body_b_naked_blanket_cover2[M_daisy.pregnancy.to_string]"
        attribute b_naked_diane_comfort "daisy_body_b_naked_diane_[M_diane.outfit.get]_comfort[M_daisy.pregnancy.to_string]"
        attribute b_naked_diane_shirtless_comfort "daisy_body_b_naked_diane_shirtless_comfort[M_daisy.pregnancy.to_string]"
        attribute b_naked_diane_comfort2 "daisy_body_b_naked_diane_[M_diane.outfit.get]_comfort2[M_daisy.pregnancy.to_string]"
        attribute b_naked_diane_shirtless_comfort2 "daisy_body_b_naked_diane_shirtless_comfort2[M_daisy.pregnancy.to_string]"


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any daisy_clothing_options auto


    group face if_not 'm_talk' if_any ['b_naked_shy','b_naked_blanket_mc2','b_naked_blanket_mc1'] auto:
        offset (-8, 10)


    group face if_not 'm_talk' if_any ['b_naked_blanket_cover1','b_naked_blanket_cover2','b_naked_blanket_cover1_pregnant_belly','b_naked_blanket_cover2_pregnant_belly'] auto:
        offset (-124, 10)


    group face if_not 'm_talk' if_any ['b_naked_cower','b_naked_cower_pregnant_belly'] auto:
        offset (62, 26)


    group face if_not 'm_talk' if_any ['b_naked_sleep'] auto:
        align (.5, .5)
        offset (502, 274)
        rotate 34
        rotate_pad False
        xzoom -1


    group face if_not 'm_talk' if_any ['b_naked_sleep_nightmare'] auto:
        align (.5, .5)
        offset (498, 278)
        rotate 34
        rotate_pad False
        xzoom -1


    group face if_not 'm_talk' if_any ['b_naked_sleep_up'] auto:
        align (.5, .5)
        offset (12, -12)
        rotate 9
        rotate_pad False





    group face if_not 'm_talk' if_any ['b_naked_behind_look'] auto variant 'naked_behind_look'







    group face if_all 'm_talk' if_any daisy_clothing_options auto variant 'talk'


    group face if_all 'm_talk' if_any ['b_naked_shy','b_naked_blanket_mc2','b_naked_blanket_mc1'] auto variant 'talk':
        offset (-8, 10)


    group face if_all 'm_talk' if_any ['b_naked_blanket_cover1','b_naked_blanket_cover2','b_naked_blanket_cover1_pregnant_belly','b_naked_blanket_cover2_pregnant_belly'] auto variant 'talk':
        offset (-124, 10)


    group face if_all 'm_talk' if_any ['b_naked_cower','b_naked_cower_pregnant_belly'] auto variant 'talk':
        offset (62, 26)


    group face if_all 'm_talk' if_any ['b_naked_sleep'] auto variant 'talk':
        align (.5, .5)
        offset (502, 274)
        rotate 34
        rotate_pad False
        xzoom -1


    group face if_all 'm_talk' if_any ['b_naked_sleep_nightmare'] auto variant 'talk':
        align (.5, .5)
        offset (498, 278)
        rotate 34
        rotate_pad False
        xzoom -1


    group face if_all 'm_talk' if_any ['b_naked_sleep_up'] auto variant 'talk':
        align (.5, .5)
        offset (12, -12)
        rotate 9
        rotate_pad False





    group face if_all 'm_talk' if_any ['b_naked_behind_look'] auto variant 'naked_behind_look_talk'



    group arms if_any ['b_naked', 'b_wet', 'b_casual', 'b_towelhead', 'b_pantieless'] auto variant 'naked':
        attribute a_idle default "characters/daisy/daisy_arms_naked[M_daisy.pregnancy.to_string]_a_sides.png"     
        attribute a_wiping_tears "daisy_arms_naked[M_daisy.pregnancy.to_string]_a_wiping_tears"
        attribute a_up "daisy_arms_naked[M_daisy.pregnancy.to_string]_a_up"   
        attribute a_touch "daisy_arms_naked[M_daisy.pregnancy.to_string]_a_touch"   
        attribute a_baby "characters/daisy/daisy_arms_naked_a_baby_[M_daisy.pregnancy.baby_gender].png"      

    group arms if_any ['b_naked_flowers'] auto variant 'naked_flowers':
        attribute a_idle default "characters/daisy/daisy_arms_naked_flowers_a_sides.png"


    group arms if_any ['b_naked_shy'] auto variant 'naked_shy':
        attribute a_idle default 'daisy_arms_naked_shy_a_front'


    group arms if_any ['b_naked_behind_look'] auto variant 'naked_behind_look':
        attribute a_idle default 'daisy_arms_naked_behind_look_a_flowers'


    group arms if_any ['b_naked_sleep_up'] auto variant 'naked_sleep_up':
        attribute a_idle default 'daisy_arms_naked_sleep_up_a_down'


    group overlay auto:
        attribute o_empty default null

image daisy_f = "characters/daisy/daisy_face_f_normal.png"

image daisy_arms_naked_a_touch = "characters/daisy/daisy_arms_naked_pregnant_bump_a_touch.png"
image daisy_arms_naked_pregnant_bump_a_touch = "characters/daisy/daisy_arms_naked_pregnant_bump_a_touch.png"
image daisy_arms_naked_pregnant_belly_a_touch = "characters/daisy/daisy_arms_naked_pregnant_belly_a_touch.png"

image daisy_arms_naked_a_wiping_tears = "characters/daisy/daisy_arms_naked_a_wiping_tears.png"
image daisy_arms_naked_pregnant_bump_a_wiping_tears = "characters/daisy/daisy_arms_naked_a_wiping_tears.png"
image daisy_arms_naked_pregnant_belly_a_wiping_tears = "characters/daisy/daisy_arms_naked_pregnant_belly_a_wiping_tears.png"

image daisy_arms_naked_a_up = "characters/daisy/daisy_arms_naked_a_up.png"
image daisy_arms_naked_pregnant_bump_a_up = "characters/daisy/daisy_arms_naked_a_up.png"
image daisy_arms_naked_pregnant_belly_a_up = "characters/daisy/daisy_arms_naked_pregnant_belly_a_up.png"

image daisy_body_b_diane_milking:
    Transform("characters/daisy/daisy_body_b_naked_milking_[M_diane.outfit.get]1.png")
    pause .4
    Transform("characters/daisy/daisy_body_b_naked_milking_[M_diane.outfit.get]2.png")
    pause .4
    repeat

image daisy_body_b_player_milking:
    Transform("characters/daisy/daisy_body_b_naked_milking1[M_daisy.pregnancy.to_string].png")
    pause .4
    Transform("characters/daisy/daisy_body_b_naked_milking2[M_daisy.pregnancy.to_string].png")
    pause .4
    repeat

image daisy_body_b_naked_boob:
    Transform("characters/daisy/daisy_body_b_naked_boob1[M_daisy.pregnancy.to_string].png")
    pause .4
    Transform("characters/daisy/daisy_body_b_naked_boob2[M_daisy.pregnancy.to_string].png")
    pause .4
    repeat

image daisy_body_b_naked_behind_pickup:
    'characters/daisy/daisy_body_b_naked_behind_pickup1.png'
    pause .4
    'characters/daisy/daisy_body_b_naked_behind_pickup2.png'
    pause .4
    repeat

image daisy_body_b_naked_cower = "characters/daisy/daisy_body_b_naked_cower.png"
image daisy_body_b_naked_cower_pregnant_bump = "characters/daisy/daisy_body_b_naked_cower.png"
image daisy_body_b_naked_cower_pregnant_belly = "characters/daisy/daisy_body_b_naked_cower_pregnant_belly.png"

image daisy_body_b_naked_blanket_cover1 = "characters/daisy/daisy_body_b_naked_blanket_cover1.png"
image daisy_body_b_naked_blanket_cover1_pregnant_bump = "characters/daisy/daisy_body_b_naked_blanket_cover1.png"
image daisy_body_b_naked_blanket_cover1_pregnant_belly = "characters/daisy/daisy_body_b_naked_blanket_cover1_pregnant_belly.png"

image daisy_body_b_naked_blanket_cover2 = "characters/daisy/daisy_body_b_naked_blanket_cover2.png"
image daisy_body_b_naked_blanket_cover2_pregnant_bump = "characters/daisy/daisy_body_b_naked_blanket_cover2.png"
image daisy_body_b_naked_blanket_cover2_pregnant_belly = "characters/daisy/daisy_body_b_naked_blanket_cover2_pregnant_belly.png"

image daisy_body_b_naked_diane_naked_comfort = "characters/daisy/daisy_body_b_naked_diane_naked_comfort.png"
image daisy_body_b_naked_diane_naked_comfort_pregnant_bump = "characters/daisy/daisy_body_b_naked_diane_naked_comfort_pregnant_bump.png"
image daisy_body_b_naked_diane_naked_comfort_pregnant_belly = "characters/daisy/daisy_body_b_naked_diane_naked_comfort_pregnant_belly.png"

image daisy_body_b_naked_diane_cow_comfort = "characters/daisy/daisy_body_b_naked_diane_cow_comfort.png"
image daisy_body_b_naked_diane_cow_comfort_pregnant_bump = "characters/daisy/daisy_body_b_naked_diane_cow_comfort_pregnant_bump.png"
image daisy_body_b_naked_diane_cow_comfort_pregnant_belly = "characters/daisy/daisy_body_b_naked_diane_cow_comfort_pregnant_belly.png"

image daisy_body_b_naked_diane_shirtless_comfort = "characters/daisy/daisy_body_b_naked_diane_shirtless_comfort.png"
image daisy_body_b_naked_diane_shirtless_comfort_pregnant_bump = "characters/daisy/daisy_body_b_naked_diane_shirtless_comfort.png"
image daisy_body_b_naked_diane_shirtless_comfort_pregnant_belly = "characters/daisy/daisy_body_b_naked_diane_shirtless_comfort_pregnant_belly.png"

image daisy_body_b_naked_diane_naked_comfort2 = "characters/daisy/daisy_body_b_naked_diane_naked_comfort2.png"
image daisy_body_b_naked_diane_naked_comfort2_pregnant_bump = "characters/daisy/daisy_body_b_naked_diane_naked_comfort2_pregnant_bump.png"
image daisy_body_b_naked_diane_naked_comfort2_pregnant_belly = "characters/daisy/daisy_body_b_naked_diane_naked_comfort2_pregnant_belly.png"

image daisy_body_b_naked_diane_cow_comfort2 = "characters/daisy/daisy_body_b_naked_diane_cow_comfort2.png"
image daisy_body_b_naked_diane_cow_comfort2_pregnant_bump = "characters/daisy/daisy_body_b_naked_diane_cow_comfort2_pregnant_bump.png"
image daisy_body_b_naked_diane_cow_comfort2_pregnant_belly = "characters/daisy/daisy_body_b_naked_diane_cow_comfort2_pregnant_belly.png"

image daisy_body_b_naked_diane_shirtless_comfort2 = "characters/daisy/daisy_body_b_naked_diane_shirtless_comfort2.png"
image daisy_body_b_naked_diane_shirtless_comfort2_pregnant_bump = "characters/daisy/daisy_body_b_naked_diane_shirtless_comfort2.png"
image daisy_body_b_naked_diane_shirtless_comfort2_pregnant_belly = "characters/daisy/daisy_body_b_naked_diane_shirtless_comfort2_pregnant_belly.png"




image daisy_sex_cum = "characters/daisy/daisy_sex_back_after_cum.png"
image daisy_sex_cum spread = "characters/daisy/daisy_sex_back_after_spread_cum.png"


image daisy_sex_flying_cum 1 = "characters/diane/layeredimage/diane_sex_back_cumshot3.png"
image daisy_sex_flying_cum 2 = "characters/diane/layeredimage/diane_sex_back_cumshot4.png"


image daisy_sex_dick_cum 1 = "characters/diane/layeredimage/diane_sex_back_mc_wet.png"
image daisy_sex_dick_cum 2 = "characters/daisy/daisy_sex_back_pullout2_wet.png"


image daisy_sex_breed_mc cumshot 1 = "characters/diane/layeredimage/diane_sex_back_cumshot1.png"
image daisy_sex_breed_mc cumshot 2 = "characters/diane/layeredimage/diane_sex_back_cumshot2.png"
image daisy_sex_breed_mc = "characters/diane/layeredimage/diane_sex_back_mc.png"


image daisy_sex_breed after = "characters/daisy/daisy_sex_back_after.png"
image daisy_sex_breed after_spread = "characters/daisy/daisy_sex_back_after_spread.png"
image daisy_sex_breed creampie = "characters/daisy/daisy_sex_back_creampie.png"
image daisy_sex_breed creampie_pullout = "characters/daisy/daisy_sex_back_creampie_pullout.png"
image daisy_sex_breed insert_and_pullout = "characters/daisy/daisy_sex_back_insert_and_pullout2.png"
image daisy_sex_breed pre_talk = "characters/daisy/daisy_sex_back_pre_talk.png"

image daisy_sex_back 1 = "characters/daisy/daisy_sex_back_anim_01.png"
image daisy_sex_back 2 = "characters/daisy/daisy_sex_back_anim_02.png"
image daisy_sex_back 3 = "characters/daisy/daisy_sex_back_anim_03.png"
image daisy_sex_back 4 = "characters/daisy/daisy_sex_back_anim_04.png"
image daisy_sex_back 5 = "characters/daisy/daisy_sex_back_anim_05.png"
image daisy_sex_back 6 = "characters/daisy/daisy_sex_back_anim_06.png"
image daisy_sex_back 7 = "characters/daisy/daisy_sex_back_anim_07.png"
image daisy_sex_back 8 = "characters/daisy/daisy_sex_back_anim_08.png"
image daisy_sex_back 9 = "characters/daisy/daisy_sex_back_anim_09.png"
image daisy_sex_back 10 = "characters/daisy/daisy_sex_back_anim_10.png"

image daisy_sex_front 1 = "characters/daisy/daisy_sex_front_anim_01.png"
image daisy_sex_front 2 = "characters/daisy/daisy_sex_front_anim_02.png"
image daisy_sex_front 3 = "characters/daisy/daisy_sex_front_anim_03.png"
image daisy_sex_front 4 = "characters/daisy/daisy_sex_front_anim_04.png"
image daisy_sex_front 5 = "characters/daisy/daisy_sex_front_anim_05.png"
image daisy_sex_front 6 = "characters/daisy/daisy_sex_front_anim_06.png"
image daisy_sex_front 7 = "characters/daisy/daisy_sex_front_anim_07.png"
image daisy_sex_front 8 = "characters/daisy/daisy_sex_front_anim_08.png"
image daisy_sex_front 9 = "characters/daisy/daisy_sex_front_anim_09.png"
image daisy_sex_front 10 = "characters/daisy/daisy_sex_front_anim_10.png"



init python hide:
    count = 9
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('daisy_sex_sleep_anim', 'daisy_sex_hayloft'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_daisy))


layeredimage daisy sex_sleep:
    attribute m_talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_calm_down default


image daisy_sex_sleep_cumshot:
    'daisy_sex_sleep_cumshot1'
    .4
    'daisy_sex_sleep_cumshot2' with fastdissolve
    .4
    'daisy_sex_sleep_cumshot3' with fastdissolve



init python hide:
    count = 8
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))

    map = (('daisy_sex_stand_anim', 'daisy_sex_garden'),)

    for src, stem in map:
        for i in frames:
            renpy.image('{} {}'.format(stem, i),
                        '{}{:02}'.format(src, i))
        
        renpy.image(stem, AnimatedImage(stem, frames, M_daisy))


layeredimage daisy sex_stand:
    attribute m_talk null

    group face if_not 'm_talk' auto
    group face if_all 'm_talk' auto variant 'talk':
        attribute f_calm default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
