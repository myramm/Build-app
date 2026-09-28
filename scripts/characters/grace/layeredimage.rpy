init:
    $ grace_clothing_options = ['b_naked_pregnant_belly','b_magic','b_dressed','b_dressed_pregnant_belly','b_lead','b_dressed_pregnant_bump','b_naked','b_shirt','b_underwear','b_shorts']

init python:


    renpy.image('grace_arms_a_empty', 'ground.png')
    renpy.image('grace_body_b_empty', 'ground.png')
    renpy.image('grace_face_f_empty', 'ground.png')
    renpy.image('grace_face_talk_f_empty', 'ground.png')


    renpy.image('grace_face_talk_f_laugh', 'grace_face_f_laugh')
    renpy.image('grace_face_talk_f_angry_yelling_closed', 'grace_face_f_angry_yelling_closed')
    renpy.image('grace_face_talk_f_angry_yelling', 'grace_face_f_angry_yelling')
    renpy.image('grace_face_talk_f_disgusted_wince', 'grace_face_f_disgusted_wince')
    renpy.image('grace_face_massage_laying_talk_f_surprised', 'grace_face_massage_laying_f_surprised')
    renpy.image('grace_face_ontop_talk_f_surprised', 'grace_face_ontop_f_surprised')


    renpy.image('grace_face_f_normal_down', 'grace_face_talk_f_normal_down')

layeredimage grace:

    yanchor config.screen_height
    ypos 1.
    xanchor config.screen_width
    xpos 1.


    group body auto:
        attribute b_dressed default "grace_body_b_dressed[M_grace.pregnancy.to_string]"
        attribute b_empty null
        attribute b_massage_mc_sexy "grace_body_b_massage_mc_sexy"
        attribute b_massage_mc_sexy_dickup "grace_body_b_massage_mc_sexy_dickup"
        attribute b_massage_mc_reg "grace_body_b_massage_mc_reg"
        attribute b_massage_mc_reg_front "grace_body_b_massage_mc_reg_front"
        attribute b_massage_odette "grace_body_b_massage_odette"
        attribute b_massage_cum "grace_body_b_massage_cum"
        attribute b_magic "grace_body_b_[M_grace.outfit.get][M_grace.pregnancy.to_string]"   


    group mouth prefix 'm':
        attribute talk null

    group face:
        attribute f_normal default null







    group face if_not 'm_talk' if_any grace_clothing_options auto


    group face if_not 'm_talk' if_all 'b_dressed_hug_mc' auto:
        offset (-38, -12)


    group face if_not 'm_talk' if_all 'b_massage' auto:
        offset (-384, -150)


    group face if_not 'm_talk' if_all 'b_gown_bed' auto:
        offset (108, 16)






    group face if_not 'm_talk' if_all 'b_ontop' auto variant 'ontop'


    group face if_not 'm_talk' if_all 'b_massage_pullout' auto variant 'ontop':
        offset (-95, -41)


    group face if_not 'm_talk' if_all 'b_massage_laying' auto variant 'massage_laying'







    group face if_all 'm_talk' if_any grace_clothing_options auto variant 'talk'


    group face if_all ['m_talk','b_dressed_hug_mc'] auto variant 'talk':
        offset (-38, -12)


    group face if_all ['m_talk','b_massage'] auto variant 'talk':
        offset (-384, -150)


    group face if_all ['m_talk','b_gown_bed'] auto variant 'talk':
        offset (108, 16)






    group face if_all ['m_talk','b_ontop'] auto variant 'ontop_talk'


    group face if_all ['m_talk','b_massage_pullout'] auto variant 'ontop_talk':
        offset (-95, -41)


    group face if_all ['m_talk','b_massage_laying'] auto variant 'massage_laying_talk'



    group arms if_any ['b_magic'] auto:
        attribute a_idle default "grace_arms_magic_a_idle[M_grace.pregnancy.to_string]"


    group arms if_any ['b_dressed', 'b_underwear'] auto variant 'dressed':
        attribute a_idle default 'grace_arms_dressed_a_idle[M_grace.pregnancy.to_string]'
        attribute a_baby "grace_arms_dressed_a_baby_[M_grace.pregnancy.baby_gender]"


    group arms if_any ['b_dressed_pregnant_belly'] auto variant 'dressed_pregnant_belly':
        attribute a_idle default 'grace_arms_dressed_pregnant_belly_a_touch'


    group arms if_all 'b_naked' auto variant 'naked':
        attribute a_idle default 'grace_arms_naked_a_hip'


    group arms if_all 'b_naked_pregnant_belly' auto variant 'naked_pregnant_belly':
        attribute a_idle default 'grace_arms_naked_pregnant_belly_a_hips'


    group arms if_any ['b_shorts'] auto variant 'shorts':
        attribute a_idle default 'grace_arms_shorts_a_remove2'
        attribute a_hip 'grace_arms_dressed_a_hip'


    group arms if_all 'b_shirt' auto variant 'shirt':
        attribute a_idle default 'grace_arms_shirt_a_hip'


    group arms if_all 'b_massage' auto variant 'massage':
        attribute a_idle default 'grace_arms_massage_a_down'


    group arms if_all 'b_gown_bed' auto variant 'gown_bed':
        attribute a_idle default "grace_arms_gown_bed_a_baby_[M_grace.pregnancy.baby_gender]"


    group overlay auto:
        attribute o_empty default null


    group overlay if_all 'b_dressed' auto variant 'dressed':
        attribute o_empty default null


layeredimage grace massage_apt:
    attribute m_talk null

    group body:
        attribute back null default
        attribute over null
        attribute pull null

    group face if_any 'back' if_not 'm_talk':
        attribute surprised 'grace_face_ontop_f_surprised'
        attribute worried 'grace_face_ontop_f_worried' default

    group face if_any 'back' if_all 'm_talk':
        attribute worried 'grace_face_ontop_talk_f_worried'

    group face if_any 'over' if_not 'm_talk':
        attribute worried 'grace_sex_mc_top_face'

    group face if_any 'over' if_all 'm_talk':
        attribute worried 'grace_sex_mc_top_face_talk'

    group face if_any 'pull' if_not 'm_talk' offset (-95, -41):
        attribute surprised 'grace_face_ontop_f_surprised'
        attribute worried 'grace_face_ontop_f_worried'

    group face if_any 'pull' if_all 'm_talk' offset (-95, -41):
        attribute worried 'grace_face_ontop_talk_f_worried'


layeredimage grace sex_apt:
    group body:
        attribute pre default 'grace_body_b_sex_solo_base'
        attribute insert 'grace_body_b_sex_solo_anim01'
        attribute cum 'grace_body_b_sex_solo_cum'
        attribute cumshot 'grace_body_b_sex_solo_base'
        attribute after 'grace_body_b_sex_solo_after_talk'

    attribute m_talk null

    group face if_not 'm_talk':
        attribute angry 'grace_face_f_sex_solo_angry'
        attribute concerned default 'grace_face_f_sex_solo_concerned'
        attribute normal 'grace_face_f_sex_solo_normal_right'

    group face if_all 'm_talk':
        attribute angry 'grace_face_talk_f_sex_solo_angry'
        attribute concerned 'grace_face_talk_f_sex_solo_concerned'
        attribute normal 'grace_face_talk_f_sex_solo_normal_right'

    group face:
        attribute exhausted 'grace_face_f_sex_solo_exhausted'
        attribute cum null
        attribute insert null

    group arms:
        attribute down default 'grace_body_b_sex_solo_base_arm_side'
        attribute head 'grace_body_b_sex_solo_base_arm_head'
        attribute cum null
        attribute insert null

    group anon:
        attribute pre 'grace_body_b_sex_solo_pre'
        attribute cumshot anim.TransitionAnimation(
            'grace_body_b_sex_solo_cumshot01', .3, Dissolve(.3),
            'grace_body_b_sex_solo_cumshot02', .3, Dissolve(.3),
            'grace_body_b_sex_solo_cumshot03')

    group cum if_all 'pre':
        attribute inside 'grace_body_b_sex_solo_after'
        attribute outside 'grace_body_b_sex_solo_after_talk_cumshot'

    group overlay if_all 'after':
        attribute inside 'grace_body_b_sex_solo_after_talk_cum'
        attribute outside 'grace_body_b_sex_solo_after_talk_cumshot'


init python hide:
    stem = 'grace_sex_apt_anim'
    count = 7
    first = 1
    frames = tuple(i % count + 1 for i in xrange(first, first + count))
    for f in frames:
        src = 'grace_body_b_sex_solo_anim{:02}'.format(f)
        renpy.image('{} {}'.format(stem, f), src)
    renpy.image(stem, AnimatedImage(stem, frames, M_grace))


image grace_f = "characters/grace/grace_face_f_normal.png"

image grace_arms_magic_a_idle = "grace_arms_[M_grace.outfit.get]_a_hip"
image grace_arms_magic_a_idle_pregnant_bump = "grace_arms_[M_grace.outfit.get]_pregnant_bump_a_touch"
image grace_arms_magic_a_idle_pregnant_belly = "grace_arms_[M_grace.outfit.get]_pregnant_belly_a_touch"

image grace_arms_dressed_a_idle = "grace_arms_dressed_a_hip"
image grace_arms_dressed_a_idle_pregnant_bump = "grace_arms_dressed_pregnant_bump_a_touch"
image grace_arms_dressed_a_idle_pregnant_belly = "grace_arms_dressed_pregnant_belly_a_touch"


image grace_sex_massage 1 = "grace_sex_anim_01"
image grace_sex_massage 2 = "grace_sex_anim_02"
image grace_sex_massage 3 = "grace_sex_anim_03"
image grace_sex_massage 4 = "grace_sex_anim_04"
image grace_sex_massage 5 = "grace_sex_anim_05"
image grace_sex_massage 6 = "grace_sex_anim_06"
image grace_sex_massage 7 = "grace_sex_anim_07"
image grace_sex_massage 8 = "grace_sex_anim_08"
image grace_sex_massage 9 = "grace_sex_anim_09"
image grace_sex_massage 10 = "grace_sex_anim_10"
image grace_sex_massage 11 = "grace_sex_anim_11"
image grace_sex_massage 12 = "grace_sex_anim_12"
image grace_sex_massage 13 = "grace_sex_anim_13"
image grace_sex_massage 14 = "grace_sex_anim_14"
image grace_sex_massage 15 = "grace_sex_anim_15"
image grace_sex_massage 16 = "grace_sex_anim_16"
image grace_sex_massage 17 = "grace_sex_anim_17"

image grace_body_b_massage_cum:
    Transform("grace_body_b_massage_cum1")
    pause .4
    Transform("grace_body_b_massage_cum2")
    pause .4
    repeat

image grace_body_b_massage_mc_sexy:
    Transform("grace_body_b_massage_mc_soft1")
    pause .4
    Transform("grace_body_b_massage_mc_soft2")
    pause .4
    repeat

image grace_body_b_massage_mc_sexy_dickup:
    Transform("grace_body_b_massage_mc_hard1")
    pause .4
    Transform("grace_body_b_massage_mc_hard2")
    pause .4
    repeat

image grace_body_b_massage_mc_soft1 = Composite(
    (1024,768),
    (0,0), "grace_body_b_massage_mc1",
    (0,0), "grace_body_b_massage_mc1_soft")

image grace_body_b_massage_mc_soft2 = Composite(
    (1024,768),
    (0,0), "grace_body_b_massage_mc2",
    (0,0), "grace_body_b_massage_mc2_soft")

image grace_body_b_massage_mc_hard1 = Composite(
    (1024,768),
    (0,0), "grace_body_b_massage_mc1",
    (0,0), "grace_body_b_massage_mc1_hard")

image grace_body_b_massage_mc_hard2 = Composite(
    (1024,768),
    (0,0), "grace_body_b_massage_mc2",
    (0,0), "grace_body_b_massage_mc2_hard")

image grace_body_b_massage_mc_reg:
    Transform("grace_body_b_massage_mc3")
    pause .4
    Transform("grace_body_b_massage_mc4")
    pause .4
    repeat

image grace_body_b_massage_mc_reg_front:
    Transform("grace_body_b_massage_mc5")
    pause .4
    Transform("grace_body_b_massage_mc6")
    pause .4
    repeat

image grace_body_b_massage_odette:
    Transform("grace_body_b_massage_odette1")
    pause .4
    Transform("grace_body_b_massage_odette2")
    pause .4
    repeat



image grace_sex_mc down_back = "grace_sex_mc_down_back"
image grace_sex_mc down_front = "grace_sex_mc_down_front"
image grace_sex_mc laying = "grace_sex_mc_laying"


image grace_sex_mc_overlay o_dick_soft = "grace_sex_mc_overlay_o_dick_soft"
image grace_sex_mc_overlay o_dick_hard = "grace_sex_mc_overlay_o_dick_hard"
image grace_sex_mc_overlay o_climb_dick_soft = "grace_sex_mc_overlay_o_climb_dick_soft"
image grace_sex_mc_overlay o_climb_dick_hard = "grace_sex_mc_overlay_o_climb_dick_hard"

image grace_sex_mc_overlay o_massage_pullout_cum:
    Transform("grace_sex_overlay_massage_pullout_o_cum1")
    pause .4
    Transform("grace_sex_overlay_massage_pullout_o_cum2")
    pause .4
    Transform("grace_sex_overlay_massage_pullout_o_cum3")





image xray_grace_massage:
    Transform("characters/xray/xray_side_01.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_02.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_03.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_04.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_05.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_06.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_07.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_08.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_09.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_10.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_11.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_12.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_13.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_14.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_15.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_16.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_17.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 0.4
    Transform("characters/xray/xray_side_18.png", xzoom=-0.55, yzoom=0.55, rotate=-135, xoffset=220, yoffset=140)
    pause 2.0
    linear 2.5 alpha 0


image xray_grace_sex_apt:
    anchor (.5, .5)
    pos (250 + 251, 250 + 214)
    rotate -22
    rotate_pad False
    zoom .9
    'xray_side'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
