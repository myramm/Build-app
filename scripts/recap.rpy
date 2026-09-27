label recap:
    scene black
    show text _ ('Previously on Summertime Saga') at truecenter with dissolve
    pause

    scene intro_01
    show text _ ('After the death of my father under suspicious circumstances...') as caption
    with fade
    pause

    scene intro_02
    show text _ ('I resolved to step in where the cops seemingly could not and solve his murder.') as caption
    with fade
    pause

    scene location_home_cutscene01
    show text _ ('All around me, life continued on, and I got swept along with it.') as caption
    with fade
    pause

    scene location_home_driveby_cutscene01
    show text _ ('But despite suffering intimidating interventions...') as caption
    with fade
    pause

    scene location_home_attic_cutscene01_night
    show text _ ('... And a few distractions along the way...') as caption
    with fade
    pause

    scene location_home_cutscene03 as cutscene
    show text _ ('... Okay, more than a few distractions.') as caption
    with fade
    pause

    python hide:
        show = ['location_school_art_cutscene07',
                'location_school_assembly_hall_cutscene02',
                'location_crypt_entrance_cutscene',
                'location_tattoo_cutscene01',
                'location_trailer_cutscene08',
                'location_boat_cutscene_03b',
                'location_tattoo_garage_cutscene03',
                'location_school_outside_school_night_cutscene03',
                'location_home_bedroom_cutscene11b',
                'location_smith_frontyard_cutscene01',
                'location_school_music_cutscene05',
                'location_tattoo_bedroom_cutscene04',
                'location_home_basement_cutscene',
                'location_school_gym_cutscene01',
                'location_pool_cutscene02',
                'location_park_bench_cutscene',
                'location_home_jennybedroom_cutscene03',
                'location_tattoo_apartment_cutscene03',
                'location_forest_altar_cutscene_night',
                'location_diane_garden_cutscene04',
                'location_beach_cutscene02']

        args = ['location_home_cutscene03', 0, fade]
        time = .4
        maxx = float(len(show)) 

        for i, s in enumerate(show):
            t = .1 + time * _warper.easeout((maxx - i) / maxx)
            args.extend((s, t * 2, Fade(t, 0, t)))

        args = args[:-2] 

        renpy.dynamic(book=anim.TransitionAnimation(*args,
                                                    anim_timebase=False))

    show expression book as cutscene
    pause sum(book.delays[:-1]) + .3

    scene location_school_french_cutscene15
    show text _ ('Fine! Countless distractions! Jeez!\n\n') as caption
    with hpunch
    pause
    show text _ ('\n\nAnyway...') as caption2 with dissolve
    pause

    scene location_mugging_cutscene05
    show text _ ('In my quest for justice, I met Tony, my boss.') as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ('As our bond deepened, he asked of me the most intimate of favours...') as caption with dissolve
    pause

    scene expression background(536, 400, 2., l='pizza_storage', t=3) as stage
    show anon a_sides b_shirt f_worried od_empty:
        xoffset 50
    show tony a_idle b_casual f_normal o_casual_boner:
        xoffset 100
    show maria a_jerk1 b_naked_bending f_sad o_idle:
        xoffset 50
    with fade
    tony "Maafkan aku, jagoan."

    tony "Aku tidak bermaksud memaksakan, hanya saja-"

    tony "Itu anakku yang kamu buat dan... Yah, aku agak-"

    tony "Saya ingin merasa menjadi bagian dari konsepsi juga, Anda tahu?"

    show anon od_dick4
    show maria b_naked_shy1 f_sad:
        xoffset 200
        xzoom -1
    with dissolve
    maria "Ya, aku tahu, sayang."

    show tony f_sad
    maria "Hal ini dapat dimengerti tetapi kita juga harus menghormati pendapat {b}[firstname]{/b}."

    maria "Lagipula, dialah yang membantu kita..."

    tony "{i}*Huh*{/i} Ya, kamu benar, sayang."

    tony "Bagaimana menurutmu, jagoan?"

    tony "Bisakah saya tinggal sampai konsepsi anak saya?"


    menu:
        "Tentu saja.":
            $ M_tony.set('watches', 'plus')
        "Tidak.":

            $ M_tony.set('watches', False)

    $ unlock_scene('maria', '01_unlocked', variant=bool(M_tony.watches))

    if M_tony.watches:
        anon f_normal "Aku tidak bisa memaksamu keluar kamar saat mengandung anakmu, {b}Tony{/b}..."

        show maria f_shy
        show tony a_wave f_normal
        with {'master': dissolve}
        tony "Terima kasih, juara!"

        tony "Anda tidak tahu betapa berartinya ini bagi saya!"

    else:

        anon "Maaf, {b}Tony{/b}."

        show tony a_sides f_sad_down with {'master': dissolve}
        anon "Kurasa aku tidak bisa melakukan ini bersamamu di kamar."

        tony "Oh."

        pause
        tony "Jadi begitu."

        maria "Tidak apa-apa, {b}[firstname]{/b}."

        maria "Anda tidak perlu menyesal."

        tony f_sad "Y-ya, {b}Maria{/b} benar."

        tony "Tidak masalah."


    scene location_warehouse_frontyard_cutscene_02
    show text _ ("And little by little, I uncovered more and more of the mob's activities.") as caption
    with gameover
    pause

    scene location_dealership_office_cutscene03
    show text _ ('Through a combination of painstaking detective work...') as caption
    with fade
    pause

    scene location_treehouse_cutscene01
    show text _ ('... and making influential friends in the unlikeliest of places.') as caption
    with fade
    pause

    scene location_school_science_cutscene02
    show text _ ('All the while staying on top of my studies, even as they seemed to fade into obscurity.') as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ('Some days it didn\'t feel like I attended school at all.') as caption with dissolve
    pause

    scene location_rump_office_cutscene01
    show text _ ('I was able to find enough hard evidence to start dismantling the seedy underbelly of Summerville.') as caption
    with fade
    pause

    scene location_warehouse_sewers_cutscene_04
    show text _ ('It was a messy job, but someone had to do it...') as caption
    with fade
    pause

    scene location_warehouse_attack_cutscene05
    show text _ ('... and yes. Mistakes were occasionally made...') as caption
    with fade
    pause

    scene location_warehouse_attack_cutscene46
    show text _ ('... but by no small miracle I was able to succeed!') as caption
    with fade
    pause

    scene location_school_french_cutscene16
    show text _ ('Throughout all this, it was my friends that helped keep me sane.') as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ('... and while I grew close with many...') as caption with dissolve
    pause

    scene location_tattoo_tent_cutscene_eve
    show text _ ('... one question from Eve always sticks with me...') as caption
    with fade
    pause

    scene location_tattoo_rooftop_ledge
    show eve a_beer_hold b_sidebed f_nervous
    show anon b_sit f_flirt:
        yoffset 20
    with fade
    eve "Bagaimana denganmu?"

    anon f_surprised @ -m_talk "Hmm?"

    eve "Bisakah Anda membayangkan diri Anda bersama pria lain?"

    show anon f_thinking

    menu:
        "Mustahil.":
            $ M_eve.set('biggus_dickus', '')
        "Mungkin.":

            $ persistent.eve_bulge_unlocked = True
            $ M_eve.set('biggus_dickus', '_alt')

    if M_eve.biggus_dickus:
        anon f_shy "Aku tidak tahu."

        anon "Saya tidak pernah memikirkannya."

        pause
        eve f_happy @ f_laugh "Ha ha ha!"

        anon f_normal "Apa?"

        eve "Nah, pikirkanlah!"

        anon "Hehe, baiklah."

        show anon f_thinking
        show eve a_beer_drink f_drink
        with {'master': dissolve}
        pause
        show eve a_beer_hold f_disgusted
        with {'master': dissolve}
        anon @ -m_talk "Hmm."

        pause
        eve f_happy "Dengan baik?!"

        show anon a_thinking
        with {'master': dissolve}
        anon "saya sedang berpikir!"

        eve @ f_laugh "Ha ha ha!"

        pause
        show anon a_lap f_shy
        with {'master': dissolve}
        anon "Saya kira saya setuju dengan Anda..."

        anon f_normal "Kepribadian lebih penting daripada gender."

        eve f_surprised "Benar-benar?"

        anon f_happy "Ya."

        eve f_nervous_down "Saya tidak mengharapkan itu."

        show eve a_beer_drink f_drink
        with dissolve
    else:

        anon f_unimpressed "Cowok itu menjijikkan!"

        eve f_happy @ f_disgusted "Jadi, maksudmu... Kamu menjijikkan?"

        anon f_normal @ f_laugh "Oh, tentu saja!"

        anon "Aku tidak tahu bagaimana kamu bisa bertahan denganku..."

        anon "... aku menjijikkan!"

        eve @ f_laugh "Ha ha ha!"

        eve "Kamu selalu tahu cara membuatku tertawa!"


    scene intro_04
    show text _ ('So now you know my story...') as caption
    with gameover
    pause
    hide caption with dissolve
    show text _ ('... where I go from here I leave in your hands...') as caption with dissolve
    pause

    scene black with Dissolve(2)
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
