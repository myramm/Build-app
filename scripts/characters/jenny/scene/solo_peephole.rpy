label scene_jenny_solo_peephole:

    return


label scene_jenny_solo_peephole.stage:
    scene location_home_attic_peep_closeup
    return


label scene_jenny_solo_peephole.animate:
    show jenny_solo_peephole_anim as animation
    return


label scene_jenny_solo_peephole.daddy:
    jenny "MM."

    pause
    jenny "Itu dia, Ayah!"

    jenny "Beri aku yang besar!"

    pause
    jenny "Haah, dua puluh empat karat..."

    jenny "... Batu kecubung bertatahkan..."

    $ M_jenny.set('sex speed', 1 / 10.)
    jenny "... Ahh, sial!"

    anon "(Hmm?)"

    pause
    jenny "Apa itu?"

    jenny "Kamu ingin mengajakku naik kapal pesiar barumu?!"

    pause
    jenny "Mmm, sampanye di bak mandi air panas?!"

    $ M_jenny.set('sex speed', 1 / 12.)
    jenny "Oh ya..."

    jenny "... Isi aku!"

    anon "( Ini yang dia pikirkan saat dia melakukan masturbasi?! )"

    pause
    jenny "Ahh, tapi aku tidak bisa memutuskan antara mobil convertible merah dan mobil hitam-"

    jenny "Ah, benarkah?"

    jenny "Kamu akan membelikan keduanya untukku?!"

    $ M_jenny.set('sex speed', 1 / 16.)
    jenny "Tidak, kamu yang terbaik!"

    pause
    return


label scene_jenny_solo_peephole.anon:
    jenny "MM."

    pause
    jenny "Itu dia!"

    jenny "Panggil aku putri!!"

    pause
    jenny "Jangan bicara balik padaku..."

    jenny "... Anda tahu Anda menginginkannya!"

    $ M_jenny.set('sex speed', 1 / 10.)
    jenny "Ahh, sial!"

    anon "(Hmm?)"

    pause
    jenny "Diam dan makan vaginaku!"

    pause
    jenny "Hmm, begitu saja."

    jenny "Oh, aku yakin kamu ingin meniduriku, bukan?"

    jenny "Katakan, {b}[firstname]{/b}!"

    anon "( !!! )"
    $ M_jenny.set('sex speed', 1 / 12.)
    jenny "Tidak, itu benar!"

    anon "(Dia sedang membayangkanku!)"

    jenny "Berlutut!"

    pause
    jenny "Sekarang jilat kakiku dan mohon padaku!"

    $ M_jenny.set('sex speed', 1 / 14.)
    jenny "Mhmm..."

    $ M_jenny.set('sex speed', 1 / 16.)
    jenny "... Semua jari kakiku."

    pause
    jenny "Ahh, sial!"

    pause
    return


label scene_jenny_solo_peephole.repeat(subject='daddy'):
    python hide:
        M_jenny.set('sex speed', 1 / 8.)

    call scene_jenny_solo_peephole.stage
    call scene_jenny_solo_peephole.animate
    with fade

    if subject == 'daddy':
        jump scene_jenny_solo_peephole.daddy

    jump scene_jenny_solo_peephole.anon


label scene_jenny_solo_peephole.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Jenny']['variants']['20_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_home_attic) with fade
        menu:
            "Ayah" if 'daddy' in variants:
                call scene_jenny_solo_peephole.repeat ('daddy')

            "[firstname]" if 'anon' in variants:
                call scene_jenny_solo_peephole.repeat ('anon')
    else:

        call scene_jenny_solo_peephole.repeat (next(iter(variants)))

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
